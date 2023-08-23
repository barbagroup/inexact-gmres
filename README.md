inexact-gmres
=============
Repository of the source files for our manuscript, submitted for peer review. Includes all the LaTeX source and image files, as well as Python plotting scripts to produce the images.

**Paper Title:**

*"Inexact GMRES iterations and relaxation strategies with fast-multipole boundary element method"*

**Tingyu Wang**[1],
**Simon K. Layton**[2]
and **Lorena A. Barba**[1]

[1] Department of Mechanical and Aerospace Engineering, The George Washington University, Washington DC, 20052
[2] Department of Mechanical Engineering, Boston University, Boston, MA 02215; currently at Nvidia, Corp., Santa Clara, CA

Preprint:
[arxiv:1506.05957](http://arxiv.org/abs/1506.05957)

Version of record:
_Advances in Computational Mathematics_, Topical Collection: Advances in Computational Integral Equations (ACIE), 2022
DOI: [10.1007/s10444-022-09932-8](https://doi.org/10.1007/s10444-022-09932-8)

**Abstract**

Boundary element methods produce dense linear systems that can be accelerated via multipole expansions. Solved with Krylov methods, this implies computing the matrix-vector products within each iteration with some error, at an accuracy controlled by the order of the expansion, *p*. We take advantage of a unique property of Krylov iterations that allow lower accuracy of the matrix-vector products as convergence proceeds, and propose a relaxation strategy based on progressively decreasing *p*. 
 In extensive numerical tests of the relaxed Krylov iterations, we obtained speed-ups of between 1.5x and 2.3x for Laplace problems and between 2.7x and 3.3x for Stokes problems. We include an application to Stokes flow around red blood cells, computing with up to 64 cells and problem size up to 131k boundary elements and nearly 400k unknowns. The study was done with an in-house multi-threaded C++ code, on a hexa-core CPU. The code is available on its version-control repository, [https://github.com/barbagroup/fmm-bem-relaxed](https://github.com/barbagroup/fmm-bem-relaxed).

Corresponding author: Lorena A. Barba [labarba@gwu.edu](mailto:labarba@gwu.edu)

This work was partially supported by the National Science Foundation under award ACI-1149784.
