# Drogon Flow model files

This repository has 100 realizations of the Drogon Flow model files. The files are based
on a run of the 24.4.0 revision found in https://github.com/equinor/fmu-drogon. The
parameters used is also included. Note that the files are based on a run with no
structural uncertainty, i.e. the grid is the same for all realizations. Hence, to reduce
storage usage, we have only uploaded the grid for realization-0 and added a symlink to
this grid in all other realizations.

Drogon is a synthetic reservoir model developed and maintained by Equinor. It includes a
complete FMU (Fast Model Update) set-up, see https://github.com/equinor/fmu-drogon for
details.

## License

This work is dual-licensed under CC-BY-4.0 and GPL-3.0 (or any later version). Please
see the files LICENSE-CCBYSA and LICENSE-GPLV3 for full details.

Data and text files in this work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

Code in this work is licensed under a [GNU General Public Version 3 License][gpl-v3].


[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]
[![GPL-V3][gpl-v3-shield]][gpl-v3]


[cc-by-sa]: https://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg

[gpl-v3]: https://www.gnu.org/licenses/gpl-3.0.en.html
[gpl-v3-shield]: https://img.shields.io/badge/License-GPLv3-blue.svg
