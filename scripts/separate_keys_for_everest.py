#!/usr/bin/env python
"""
Extract keywords from ECLIPSE/OPM Flow input file.

This script creates new files with only the selected keywords included.
These new files can used as an include files for the schedule file.
It organizes information per well in separate files.

It handles multiple instances of the same keyword.
It handles keywords that have the well mentioned only in the first line.
It skips wells that are not of interest.
It is used to prepare files for the Everest tutorial.
"""

import os


def find_keyword_positions(file, keyword):
    """Find the positions of a keyword in a file."""

    # find keyword line numbers
    keyword_found = False
    begin_idx = []
    end_idx = []
    with open(file, "r") as f:
        # get indexes of the beginning and end of each keyword
        for i, line in enumerate(f):
            if keyword in line:
                begin_idx.append(i)
                keyword_found = True
            if keyword_found and "/" in line.split()[0]:
                # line begins with '/'
                end_idx.append(i)
                keyword_found = False

    return begin_idx, end_idx


def get_all_lines_to_write(lines, n, begin_idx, end_idx, well):
    """Gather all lines for keyword instance if it contains well"""

    # check if well is in the keyword instance at least once
    lines_to_write = range(begin_idx[n], end_idx[n] + 1)
    well_found = False
    for i in lines_to_write:
        if well in lines[i]:
            well_found = True

    return lines_to_write, well_found


def get_lines_to_write(lines, n, begin_idx, end_idx, well, wells_to_skip):
    """Gather lines for keyword instance which contain well
    but do not contain wells to skip"""

    lines_to_write = [begin_idx[n]]
    # check if well is in the keyword instance
    well_found = False
    for i in range(begin_idx[n] + 1, end_idx[n]):
        if "--" in lines[i]:
            lines_to_write.append(i)
        # make sure skipepd wells are not included
        if well in lines[i] and not any(s in lines[i] for s in wells_to_skip):
            well_found = True
            lines_to_write.append(i)
    lines_to_write.append(end_idx[n])

    return lines_to_write, well_found


def write_keyword_to_file(
    input_file,
    output_file,
    begin_idx,
    end_idx,
    keyword,
    well,
    wells_to_skip,
):
    """Write the well info from keyword to a file."""

    with open(input_file, "r") as f:

        # make sure directory output exists
        dir_output = os.path.dirname(input_file)
        if not os.path.exists(dir_output):
            os.makedirs(dir_output)

        # if well is found in the keyword instance, write it to file
        with open(output_file, "a") as g:
            lines = f.readlines()
            for n in range(len(begin_idx)):
                if keyword in keywords_individual:
                    lines_to_write, well_found = get_all_lines_to_write(
                        lines, n, begin_idx, end_idx, well
                    )
                else:
                    lines_to_write, well_found = get_lines_to_write(
                        lines, n, begin_idx, end_idx, well, wells_to_skip
                    )
                if well_found:
                    for i in lines_to_write:
                        g.write(lines[i])


realizations = range(100)
wells = ["A1", "A2", "A3", "A4", "A5", "A6"]

keywords = [
    "WELSPECS",
    "COMPDAT",
    "COMPLUMP",
    "COMPORD",
    "WELSEGS",
    "WSEGVALV",
    "COMPSEGS",
]
# indicate that for these keywords the well is mentioned only in the first line
# special treatment is needed for these keywords
keywords_individual = [
    "WELSEGS",
    "COMPSEGS",
]
root = "realization-{realization}/iter-0/eclipse/include/schedule/"
files = [os.path.join(root, "drogon_hist.sch")]
wells_to_skip = ["R_A1", "R_A2", "R_A3", "R_A4", "R_A5", "R_A6"]

for realization in realizations:
    for well in wells:

        output_file = os.path.join(
            root.format(realization=realization),
            f"{well}.sch",
        )
        with open(output_file, "w") as f:
            pass

        for keyword in keywords:
            for file in files:

                input_file = file.format(realization=realization)
                begin_idx, end_idx = find_keyword_positions(
                    input_file,
                    keyword,
                )
                write_keyword_to_file(
                    input_file,
                    output_file,
                    begin_idx,
                    end_idx,
                    keyword,
                    well,
                    wells_to_skip,
                )
