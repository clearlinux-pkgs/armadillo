#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : armadillo
Version  : 9.600.4
Release  : 8
URL      : http://sourceforge.net/projects/arma/files/armadillo-9.600.4.tar.xz
Source0  : http://sourceforge.net/projects/arma/files/armadillo-9.600.4.tar.xz
Summary  : C++ linear algebra library
Group    : Development/Tools
License  : Apache-2.0
Requires: armadillo-data = %{version}-%{release}
Requires: armadillo-lib = %{version}-%{release}
Requires: armadillo-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : hdf5-dev
BuildRequires : pkg-config

%description
Armadillo is a high quality C++ library for linear algebra and scientific computing,
aiming towards a good balance between speed and ease of use.
Useful for algorithm development directly in C++,
and/or quick conversion of research code into production environments.
The syntax (API) is deliberately similar to Matlab.
The library provides efficient classes for vectors, matrices and cubes,
as well as 200+ associated functions (eg. contiguous and non-contiguous
submatrix views).  Various matrix decompositions are provided through
integration with LAPACK, or one of its high performance drop-in replacements
(eg. OpenBLAS, Intel MKL, Apple Accelerate framework, etc).
A sophisticated expression evaluator (via C++ template meta-programming)
automatically combines several operations (at compile time) to increase
speed and efficiency.
The library can be used for machine learning, pattern recognition,
computer vision, signal processing, bioinformatics, statistics, finance, etc.

%package data
Summary: data components for the armadillo package.
Group: Data

%description data
data components for the armadillo package.


%package dev
Summary: dev components for the armadillo package.
Group: Development
Requires: armadillo-lib = %{version}-%{release}
Requires: armadillo-data = %{version}-%{release}
Provides: armadillo-devel = %{version}-%{release}
Requires: armadillo = %{version}-%{release}
Requires: armadillo = %{version}-%{release}

%description dev
dev components for the armadillo package.


%package lib
Summary: lib components for the armadillo package.
Group: Libraries
Requires: armadillo-data = %{version}-%{release}
Requires: armadillo-license = %{version}-%{release}

%description lib
lib components for the armadillo package.


%package license
Summary: license components for the armadillo package.
Group: Default

%description license
license components for the armadillo package.


%prep
%setup -q -n armadillo-9.600.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1563158345
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1563158345
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/armadillo
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/armadillo/LICENSE.txt
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/Armadillo/CMake/ArmadilloConfig.cmake
/usr/share/Armadillo/CMake/ArmadilloConfigVersion.cmake
/usr/share/Armadillo/CMake/ArmadilloLibraryDepends-relwithdebinfo.cmake
/usr/share/Armadillo/CMake/ArmadilloLibraryDepends.cmake

%files dev
%defattr(-,root,root,-)
/usr/include/armadillo
/usr/include/armadillo_bits/BaseCube_bones.hpp
/usr/include/armadillo_bits/BaseCube_meat.hpp
/usr/include/armadillo_bits/Base_bones.hpp
/usr/include/armadillo_bits/Base_meat.hpp
/usr/include/armadillo_bits/Col_bones.hpp
/usr/include/armadillo_bits/Col_meat.hpp
/usr/include/armadillo_bits/Cube_bones.hpp
/usr/include/armadillo_bits/Cube_meat.hpp
/usr/include/armadillo_bits/GenCube_bones.hpp
/usr/include/armadillo_bits/GenCube_meat.hpp
/usr/include/armadillo_bits/GenSpecialiser.hpp
/usr/include/armadillo_bits/Gen_bones.hpp
/usr/include/armadillo_bits/Gen_meat.hpp
/usr/include/armadillo_bits/GlueCube_bones.hpp
/usr/include/armadillo_bits/GlueCube_meat.hpp
/usr/include/armadillo_bits/Glue_bones.hpp
/usr/include/armadillo_bits/Glue_meat.hpp
/usr/include/armadillo_bits/MapMat_bones.hpp
/usr/include/armadillo_bits/MapMat_meat.hpp
/usr/include/armadillo_bits/Mat_bones.hpp
/usr/include/armadillo_bits/Mat_meat.hpp
/usr/include/armadillo_bits/OpCube_bones.hpp
/usr/include/armadillo_bits/OpCube_meat.hpp
/usr/include/armadillo_bits/Op_bones.hpp
/usr/include/armadillo_bits/Op_meat.hpp
/usr/include/armadillo_bits/Proxy.hpp
/usr/include/armadillo_bits/ProxyCube.hpp
/usr/include/armadillo_bits/Row_bones.hpp
/usr/include/armadillo_bits/Row_meat.hpp
/usr/include/armadillo_bits/SizeCube_bones.hpp
/usr/include/armadillo_bits/SizeCube_meat.hpp
/usr/include/armadillo_bits/SizeMat_bones.hpp
/usr/include/armadillo_bits/SizeMat_meat.hpp
/usr/include/armadillo_bits/SpBase_bones.hpp
/usr/include/armadillo_bits/SpBase_meat.hpp
/usr/include/armadillo_bits/SpCol_bones.hpp
/usr/include/armadillo_bits/SpCol_meat.hpp
/usr/include/armadillo_bits/SpGlue_bones.hpp
/usr/include/armadillo_bits/SpGlue_meat.hpp
/usr/include/armadillo_bits/SpMat_bones.hpp
/usr/include/armadillo_bits/SpMat_iterators_meat.hpp
/usr/include/armadillo_bits/SpMat_meat.hpp
/usr/include/armadillo_bits/SpOp_bones.hpp
/usr/include/armadillo_bits/SpOp_meat.hpp
/usr/include/armadillo_bits/SpProxy.hpp
/usr/include/armadillo_bits/SpRow_bones.hpp
/usr/include/armadillo_bits/SpRow_meat.hpp
/usr/include/armadillo_bits/SpSubview_bones.hpp
/usr/include/armadillo_bits/SpSubview_iterators_meat.hpp
/usr/include/armadillo_bits/SpSubview_meat.hpp
/usr/include/armadillo_bits/SpToDOp_bones.hpp
/usr/include/armadillo_bits/SpToDOp_meat.hpp
/usr/include/armadillo_bits/SpValProxy_bones.hpp
/usr/include/armadillo_bits/SpValProxy_meat.hpp
/usr/include/armadillo_bits/access.hpp
/usr/include/armadillo_bits/arma_cmath.hpp
/usr/include/armadillo_bits/arma_config.hpp
/usr/include/armadillo_bits/arma_forward.hpp
/usr/include/armadillo_bits/arma_ostream_bones.hpp
/usr/include/armadillo_bits/arma_ostream_meat.hpp
/usr/include/armadillo_bits/arma_rel_comparators.hpp
/usr/include/armadillo_bits/arma_rng.hpp
/usr/include/armadillo_bits/arma_rng_cxx11.hpp
/usr/include/armadillo_bits/arma_rng_cxx98.hpp
/usr/include/armadillo_bits/arma_static_check.hpp
/usr/include/armadillo_bits/arma_str.hpp
/usr/include/armadillo_bits/arma_version.hpp
/usr/include/armadillo_bits/arrayops_bones.hpp
/usr/include/armadillo_bits/arrayops_meat.hpp
/usr/include/armadillo_bits/auxlib_bones.hpp
/usr/include/armadillo_bits/auxlib_meat.hpp
/usr/include/armadillo_bits/band_helper.hpp
/usr/include/armadillo_bits/compiler_extra.hpp
/usr/include/armadillo_bits/compiler_setup.hpp
/usr/include/armadillo_bits/compiler_setup_post.hpp
/usr/include/armadillo_bits/cond_rel_bones.hpp
/usr/include/armadillo_bits/cond_rel_meat.hpp
/usr/include/armadillo_bits/config.hpp
/usr/include/armadillo_bits/constants.hpp
/usr/include/armadillo_bits/constants_old.hpp
/usr/include/armadillo_bits/debug.hpp
/usr/include/armadillo_bits/def_arpack.hpp
/usr/include/armadillo_bits/def_atlas.hpp
/usr/include/armadillo_bits/def_blas.hpp
/usr/include/armadillo_bits/def_hdf5.hpp
/usr/include/armadillo_bits/def_lapack.hpp
/usr/include/armadillo_bits/def_superlu.hpp
/usr/include/armadillo_bits/diagmat_proxy.hpp
/usr/include/armadillo_bits/diagview_bones.hpp
/usr/include/armadillo_bits/diagview_meat.hpp
/usr/include/armadillo_bits/diskio_bones.hpp
/usr/include/armadillo_bits/diskio_meat.hpp
/usr/include/armadillo_bits/distr_param.hpp
/usr/include/armadillo_bits/eGlueCube_bones.hpp
/usr/include/armadillo_bits/eGlueCube_meat.hpp
/usr/include/armadillo_bits/eGlue_bones.hpp
/usr/include/armadillo_bits/eGlue_meat.hpp
/usr/include/armadillo_bits/eOpCube_bones.hpp
/usr/include/armadillo_bits/eOpCube_meat.hpp
/usr/include/armadillo_bits/eOp_bones.hpp
/usr/include/armadillo_bits/eOp_meat.hpp
/usr/include/armadillo_bits/eglue_core_bones.hpp
/usr/include/armadillo_bits/eglue_core_meat.hpp
/usr/include/armadillo_bits/eop_aux.hpp
/usr/include/armadillo_bits/eop_core_bones.hpp
/usr/include/armadillo_bits/eop_core_meat.hpp
/usr/include/armadillo_bits/fft_engine.hpp
/usr/include/armadillo_bits/field_bones.hpp
/usr/include/armadillo_bits/field_meat.hpp
/usr/include/armadillo_bits/fn_accu.hpp
/usr/include/armadillo_bits/fn_all.hpp
/usr/include/armadillo_bits/fn_any.hpp
/usr/include/armadillo_bits/fn_approx_equal.hpp
/usr/include/armadillo_bits/fn_as_scalar.hpp
/usr/include/armadillo_bits/fn_chi2rnd.hpp
/usr/include/armadillo_bits/fn_chol.hpp
/usr/include/armadillo_bits/fn_clamp.hpp
/usr/include/armadillo_bits/fn_cond.hpp
/usr/include/armadillo_bits/fn_conv.hpp
/usr/include/armadillo_bits/fn_conv_to.hpp
/usr/include/armadillo_bits/fn_cor.hpp
/usr/include/armadillo_bits/fn_cov.hpp
/usr/include/armadillo_bits/fn_cross.hpp
/usr/include/armadillo_bits/fn_cumprod.hpp
/usr/include/armadillo_bits/fn_cumsum.hpp
/usr/include/armadillo_bits/fn_det.hpp
/usr/include/armadillo_bits/fn_diagmat.hpp
/usr/include/armadillo_bits/fn_diagvec.hpp
/usr/include/armadillo_bits/fn_diff.hpp
/usr/include/armadillo_bits/fn_dot.hpp
/usr/include/armadillo_bits/fn_eig_gen.hpp
/usr/include/armadillo_bits/fn_eig_pair.hpp
/usr/include/armadillo_bits/fn_eig_sym.hpp
/usr/include/armadillo_bits/fn_eigs_gen.hpp
/usr/include/armadillo_bits/fn_eigs_sym.hpp
/usr/include/armadillo_bits/fn_elem.hpp
/usr/include/armadillo_bits/fn_eps.hpp
/usr/include/armadillo_bits/fn_expmat.hpp
/usr/include/armadillo_bits/fn_eye.hpp
/usr/include/armadillo_bits/fn_fft.hpp
/usr/include/armadillo_bits/fn_fft2.hpp
/usr/include/armadillo_bits/fn_find.hpp
/usr/include/armadillo_bits/fn_find_unique.hpp
/usr/include/armadillo_bits/fn_flip.hpp
/usr/include/armadillo_bits/fn_hess.hpp
/usr/include/armadillo_bits/fn_hist.hpp
/usr/include/armadillo_bits/fn_histc.hpp
/usr/include/armadillo_bits/fn_index_max.hpp
/usr/include/armadillo_bits/fn_index_min.hpp
/usr/include/armadillo_bits/fn_inplace_strans.hpp
/usr/include/armadillo_bits/fn_inplace_trans.hpp
/usr/include/armadillo_bits/fn_interp1.hpp
/usr/include/armadillo_bits/fn_interp2.hpp
/usr/include/armadillo_bits/fn_intersect.hpp
/usr/include/armadillo_bits/fn_inv.hpp
/usr/include/armadillo_bits/fn_join.hpp
/usr/include/armadillo_bits/fn_kmeans.hpp
/usr/include/armadillo_bits/fn_kron.hpp
/usr/include/armadillo_bits/fn_log_det.hpp
/usr/include/armadillo_bits/fn_logmat.hpp
/usr/include/armadillo_bits/fn_lu.hpp
/usr/include/armadillo_bits/fn_max.hpp
/usr/include/armadillo_bits/fn_mean.hpp
/usr/include/armadillo_bits/fn_median.hpp
/usr/include/armadillo_bits/fn_min.hpp
/usr/include/armadillo_bits/fn_misc.hpp
/usr/include/armadillo_bits/fn_mvnrnd.hpp
/usr/include/armadillo_bits/fn_n_unique.hpp
/usr/include/armadillo_bits/fn_nonzeros.hpp
/usr/include/armadillo_bits/fn_norm.hpp
/usr/include/armadillo_bits/fn_normalise.hpp
/usr/include/armadillo_bits/fn_normcdf.hpp
/usr/include/armadillo_bits/fn_normpdf.hpp
/usr/include/armadillo_bits/fn_numel.hpp
/usr/include/armadillo_bits/fn_ones.hpp
/usr/include/armadillo_bits/fn_orth_null.hpp
/usr/include/armadillo_bits/fn_pinv.hpp
/usr/include/armadillo_bits/fn_polyfit.hpp
/usr/include/armadillo_bits/fn_polyval.hpp
/usr/include/armadillo_bits/fn_princomp.hpp
/usr/include/armadillo_bits/fn_prod.hpp
/usr/include/armadillo_bits/fn_qr.hpp
/usr/include/armadillo_bits/fn_qz.hpp
/usr/include/armadillo_bits/fn_randg.hpp
/usr/include/armadillo_bits/fn_randi.hpp
/usr/include/armadillo_bits/fn_randn.hpp
/usr/include/armadillo_bits/fn_randu.hpp
/usr/include/armadillo_bits/fn_range.hpp
/usr/include/armadillo_bits/fn_rank.hpp
/usr/include/armadillo_bits/fn_regspace.hpp
/usr/include/armadillo_bits/fn_repelem.hpp
/usr/include/armadillo_bits/fn_repmat.hpp
/usr/include/armadillo_bits/fn_reshape.hpp
/usr/include/armadillo_bits/fn_resize.hpp
/usr/include/armadillo_bits/fn_reverse.hpp
/usr/include/armadillo_bits/fn_roots.hpp
/usr/include/armadillo_bits/fn_schur.hpp
/usr/include/armadillo_bits/fn_shift.hpp
/usr/include/armadillo_bits/fn_shuffle.hpp
/usr/include/armadillo_bits/fn_size.hpp
/usr/include/armadillo_bits/fn_solve.hpp
/usr/include/armadillo_bits/fn_sort.hpp
/usr/include/armadillo_bits/fn_sort_index.hpp
/usr/include/armadillo_bits/fn_speye.hpp
/usr/include/armadillo_bits/fn_spones.hpp
/usr/include/armadillo_bits/fn_sprandn.hpp
/usr/include/armadillo_bits/fn_sprandu.hpp
/usr/include/armadillo_bits/fn_spsolve.hpp
/usr/include/armadillo_bits/fn_sqrtmat.hpp
/usr/include/armadillo_bits/fn_stddev.hpp
/usr/include/armadillo_bits/fn_strans.hpp
/usr/include/armadillo_bits/fn_sum.hpp
/usr/include/armadillo_bits/fn_svd.hpp
/usr/include/armadillo_bits/fn_svds.hpp
/usr/include/armadillo_bits/fn_syl_lyap.hpp
/usr/include/armadillo_bits/fn_symmat.hpp
/usr/include/armadillo_bits/fn_toeplitz.hpp
/usr/include/armadillo_bits/fn_trace.hpp
/usr/include/armadillo_bits/fn_trans.hpp
/usr/include/armadillo_bits/fn_trapz.hpp
/usr/include/armadillo_bits/fn_trig.hpp
/usr/include/armadillo_bits/fn_trimat.hpp
/usr/include/armadillo_bits/fn_trunc_exp.hpp
/usr/include/armadillo_bits/fn_trunc_log.hpp
/usr/include/armadillo_bits/fn_unique.hpp
/usr/include/armadillo_bits/fn_var.hpp
/usr/include/armadillo_bits/fn_vectorise.hpp
/usr/include/armadillo_bits/fn_wishrnd.hpp
/usr/include/armadillo_bits/fn_zeros.hpp
/usr/include/armadillo_bits/glue_affmul_bones.hpp
/usr/include/armadillo_bits/glue_affmul_meat.hpp
/usr/include/armadillo_bits/glue_atan2_bones.hpp
/usr/include/armadillo_bits/glue_atan2_meat.hpp
/usr/include/armadillo_bits/glue_conv_bones.hpp
/usr/include/armadillo_bits/glue_conv_meat.hpp
/usr/include/armadillo_bits/glue_cor_bones.hpp
/usr/include/armadillo_bits/glue_cor_meat.hpp
/usr/include/armadillo_bits/glue_cov_bones.hpp
/usr/include/armadillo_bits/glue_cov_meat.hpp
/usr/include/armadillo_bits/glue_cross_bones.hpp
/usr/include/armadillo_bits/glue_cross_meat.hpp
/usr/include/armadillo_bits/glue_hist_bones.hpp
/usr/include/armadillo_bits/glue_hist_meat.hpp
/usr/include/armadillo_bits/glue_histc_bones.hpp
/usr/include/armadillo_bits/glue_histc_meat.hpp
/usr/include/armadillo_bits/glue_hypot_bones.hpp
/usr/include/armadillo_bits/glue_hypot_meat.hpp
/usr/include/armadillo_bits/glue_intersect_bones.hpp
/usr/include/armadillo_bits/glue_intersect_meat.hpp
/usr/include/armadillo_bits/glue_join_bones.hpp
/usr/include/armadillo_bits/glue_join_meat.hpp
/usr/include/armadillo_bits/glue_kron_bones.hpp
/usr/include/armadillo_bits/glue_kron_meat.hpp
/usr/include/armadillo_bits/glue_max_bones.hpp
/usr/include/armadillo_bits/glue_max_meat.hpp
/usr/include/armadillo_bits/glue_min_bones.hpp
/usr/include/armadillo_bits/glue_min_meat.hpp
/usr/include/armadillo_bits/glue_mixed_bones.hpp
/usr/include/armadillo_bits/glue_mixed_meat.hpp
/usr/include/armadillo_bits/glue_mvnrnd_bones.hpp
/usr/include/armadillo_bits/glue_mvnrnd_meat.hpp
/usr/include/armadillo_bits/glue_polyfit_bones.hpp
/usr/include/armadillo_bits/glue_polyfit_meat.hpp
/usr/include/armadillo_bits/glue_polyval_bones.hpp
/usr/include/armadillo_bits/glue_polyval_meat.hpp
/usr/include/armadillo_bits/glue_relational_bones.hpp
/usr/include/armadillo_bits/glue_relational_meat.hpp
/usr/include/armadillo_bits/glue_solve_bones.hpp
/usr/include/armadillo_bits/glue_solve_meat.hpp
/usr/include/armadillo_bits/glue_times_bones.hpp
/usr/include/armadillo_bits/glue_times_meat.hpp
/usr/include/armadillo_bits/glue_toeplitz_bones.hpp
/usr/include/armadillo_bits/glue_toeplitz_meat.hpp
/usr/include/armadillo_bits/glue_trapz_bones.hpp
/usr/include/armadillo_bits/glue_trapz_meat.hpp
/usr/include/armadillo_bits/gmm_diag_bones.hpp
/usr/include/armadillo_bits/gmm_diag_meat.hpp
/usr/include/armadillo_bits/gmm_full_bones.hpp
/usr/include/armadillo_bits/gmm_full_meat.hpp
/usr/include/armadillo_bits/gmm_misc_bones.hpp
/usr/include/armadillo_bits/gmm_misc_meat.hpp
/usr/include/armadillo_bits/hdf5_misc.hpp
/usr/include/armadillo_bits/include_atlas.hpp
/usr/include/armadillo_bits/include_hdf5.hpp
/usr/include/armadillo_bits/include_superlu.hpp
/usr/include/armadillo_bits/injector_bones.hpp
/usr/include/armadillo_bits/injector_meat.hpp
/usr/include/armadillo_bits/memory.hpp
/usr/include/armadillo_bits/mp_misc.hpp
/usr/include/armadillo_bits/mtGlueCube_bones.hpp
/usr/include/armadillo_bits/mtGlueCube_meat.hpp
/usr/include/armadillo_bits/mtGlue_bones.hpp
/usr/include/armadillo_bits/mtGlue_meat.hpp
/usr/include/armadillo_bits/mtOpCube_bones.hpp
/usr/include/armadillo_bits/mtOpCube_meat.hpp
/usr/include/armadillo_bits/mtOp_bones.hpp
/usr/include/armadillo_bits/mtOp_meat.hpp
/usr/include/armadillo_bits/mtSpGlue_bones.hpp
/usr/include/armadillo_bits/mtSpGlue_meat.hpp
/usr/include/armadillo_bits/mtSpOp_bones.hpp
/usr/include/armadillo_bits/mtSpOp_meat.hpp
/usr/include/armadillo_bits/mul_gemm.hpp
/usr/include/armadillo_bits/mul_gemm_mixed.hpp
/usr/include/armadillo_bits/mul_gemv.hpp
/usr/include/armadillo_bits/mul_herk.hpp
/usr/include/armadillo_bits/mul_syrk.hpp
/usr/include/armadillo_bits/newarp_DenseGenMatProd_bones.hpp
/usr/include/armadillo_bits/newarp_DenseGenMatProd_meat.hpp
/usr/include/armadillo_bits/newarp_DoubleShiftQR_bones.hpp
/usr/include/armadillo_bits/newarp_DoubleShiftQR_meat.hpp
/usr/include/armadillo_bits/newarp_EigsSelect.hpp
/usr/include/armadillo_bits/newarp_GenEigsSolver_bones.hpp
/usr/include/armadillo_bits/newarp_GenEigsSolver_meat.hpp
/usr/include/armadillo_bits/newarp_SortEigenvalue.hpp
/usr/include/armadillo_bits/newarp_SparseGenMatProd_bones.hpp
/usr/include/armadillo_bits/newarp_SparseGenMatProd_meat.hpp
/usr/include/armadillo_bits/newarp_SymEigsSolver_bones.hpp
/usr/include/armadillo_bits/newarp_SymEigsSolver_meat.hpp
/usr/include/armadillo_bits/newarp_TridiagEigen_bones.hpp
/usr/include/armadillo_bits/newarp_TridiagEigen_meat.hpp
/usr/include/armadillo_bits/newarp_UpperHessenbergEigen_bones.hpp
/usr/include/armadillo_bits/newarp_UpperHessenbergEigen_meat.hpp
/usr/include/armadillo_bits/newarp_UpperHessenbergQR_bones.hpp
/usr/include/armadillo_bits/newarp_UpperHessenbergQR_meat.hpp
/usr/include/armadillo_bits/newarp_cx_attrib.hpp
/usr/include/armadillo_bits/op_all_bones.hpp
/usr/include/armadillo_bits/op_all_meat.hpp
/usr/include/armadillo_bits/op_any_bones.hpp
/usr/include/armadillo_bits/op_any_meat.hpp
/usr/include/armadillo_bits/op_chi2rnd_bones.hpp
/usr/include/armadillo_bits/op_chi2rnd_meat.hpp
/usr/include/armadillo_bits/op_chol_bones.hpp
/usr/include/armadillo_bits/op_chol_meat.hpp
/usr/include/armadillo_bits/op_clamp_bones.hpp
/usr/include/armadillo_bits/op_clamp_meat.hpp
/usr/include/armadillo_bits/op_cond_bones.hpp
/usr/include/armadillo_bits/op_cond_meat.hpp
/usr/include/armadillo_bits/op_cor_bones.hpp
/usr/include/armadillo_bits/op_cor_meat.hpp
/usr/include/armadillo_bits/op_cov_bones.hpp
/usr/include/armadillo_bits/op_cov_meat.hpp
/usr/include/armadillo_bits/op_cumprod_bones.hpp
/usr/include/armadillo_bits/op_cumprod_meat.hpp
/usr/include/armadillo_bits/op_cumsum_bones.hpp
/usr/include/armadillo_bits/op_cumsum_meat.hpp
/usr/include/armadillo_bits/op_cx_scalar_bones.hpp
/usr/include/armadillo_bits/op_cx_scalar_meat.hpp
/usr/include/armadillo_bits/op_diagmat_bones.hpp
/usr/include/armadillo_bits/op_diagmat_meat.hpp
/usr/include/armadillo_bits/op_diagvec_bones.hpp
/usr/include/armadillo_bits/op_diagvec_meat.hpp
/usr/include/armadillo_bits/op_diff_bones.hpp
/usr/include/armadillo_bits/op_diff_meat.hpp
/usr/include/armadillo_bits/op_dot_bones.hpp
/usr/include/armadillo_bits/op_dot_meat.hpp
/usr/include/armadillo_bits/op_dotext_bones.hpp
/usr/include/armadillo_bits/op_dotext_meat.hpp
/usr/include/armadillo_bits/op_expmat_bones.hpp
/usr/include/armadillo_bits/op_expmat_meat.hpp
/usr/include/armadillo_bits/op_fft_bones.hpp
/usr/include/armadillo_bits/op_fft_meat.hpp
/usr/include/armadillo_bits/op_find_bones.hpp
/usr/include/armadillo_bits/op_find_meat.hpp
/usr/include/armadillo_bits/op_find_unique_bones.hpp
/usr/include/armadillo_bits/op_find_unique_meat.hpp
/usr/include/armadillo_bits/op_flip_bones.hpp
/usr/include/armadillo_bits/op_flip_meat.hpp
/usr/include/armadillo_bits/op_hist_bones.hpp
/usr/include/armadillo_bits/op_hist_meat.hpp
/usr/include/armadillo_bits/op_htrans_bones.hpp
/usr/include/armadillo_bits/op_htrans_meat.hpp
/usr/include/armadillo_bits/op_index_max_bones.hpp
/usr/include/armadillo_bits/op_index_max_meat.hpp
/usr/include/armadillo_bits/op_index_min_bones.hpp
/usr/include/armadillo_bits/op_index_min_meat.hpp
/usr/include/armadillo_bits/op_inv_bones.hpp
/usr/include/armadillo_bits/op_inv_meat.hpp
/usr/include/armadillo_bits/op_logmat_bones.hpp
/usr/include/armadillo_bits/op_logmat_meat.hpp
/usr/include/armadillo_bits/op_max_bones.hpp
/usr/include/armadillo_bits/op_max_meat.hpp
/usr/include/armadillo_bits/op_mean_bones.hpp
/usr/include/armadillo_bits/op_mean_meat.hpp
/usr/include/armadillo_bits/op_median_bones.hpp
/usr/include/armadillo_bits/op_median_meat.hpp
/usr/include/armadillo_bits/op_min_bones.hpp
/usr/include/armadillo_bits/op_min_meat.hpp
/usr/include/armadillo_bits/op_misc_bones.hpp
/usr/include/armadillo_bits/op_misc_meat.hpp
/usr/include/armadillo_bits/op_nonzeros_bones.hpp
/usr/include/armadillo_bits/op_nonzeros_meat.hpp
/usr/include/armadillo_bits/op_norm_bones.hpp
/usr/include/armadillo_bits/op_norm_meat.hpp
/usr/include/armadillo_bits/op_normalise_bones.hpp
/usr/include/armadillo_bits/op_normalise_meat.hpp
/usr/include/armadillo_bits/op_orth_null_bones.hpp
/usr/include/armadillo_bits/op_orth_null_meat.hpp
/usr/include/armadillo_bits/op_pinv_bones.hpp
/usr/include/armadillo_bits/op_pinv_meat.hpp
/usr/include/armadillo_bits/op_princomp_bones.hpp
/usr/include/armadillo_bits/op_princomp_meat.hpp
/usr/include/armadillo_bits/op_prod_bones.hpp
/usr/include/armadillo_bits/op_prod_meat.hpp
/usr/include/armadillo_bits/op_range_bones.hpp
/usr/include/armadillo_bits/op_range_meat.hpp
/usr/include/armadillo_bits/op_relational_bones.hpp
/usr/include/armadillo_bits/op_relational_meat.hpp
/usr/include/armadillo_bits/op_repelem_bones.hpp
/usr/include/armadillo_bits/op_repelem_meat.hpp
/usr/include/armadillo_bits/op_repmat_bones.hpp
/usr/include/armadillo_bits/op_repmat_meat.hpp
/usr/include/armadillo_bits/op_reshape_bones.hpp
/usr/include/armadillo_bits/op_reshape_meat.hpp
/usr/include/armadillo_bits/op_resize_bones.hpp
/usr/include/armadillo_bits/op_resize_meat.hpp
/usr/include/armadillo_bits/op_reverse_bones.hpp
/usr/include/armadillo_bits/op_reverse_meat.hpp
/usr/include/armadillo_bits/op_roots_bones.hpp
/usr/include/armadillo_bits/op_roots_meat.hpp
/usr/include/armadillo_bits/op_shift_bones.hpp
/usr/include/armadillo_bits/op_shift_meat.hpp
/usr/include/armadillo_bits/op_shuffle_bones.hpp
/usr/include/armadillo_bits/op_shuffle_meat.hpp
/usr/include/armadillo_bits/op_sort_bones.hpp
/usr/include/armadillo_bits/op_sort_index_bones.hpp
/usr/include/armadillo_bits/op_sort_index_meat.hpp
/usr/include/armadillo_bits/op_sort_meat.hpp
/usr/include/armadillo_bits/op_sp_minus_bones.hpp
/usr/include/armadillo_bits/op_sp_minus_meat.hpp
/usr/include/armadillo_bits/op_sp_plus_bones.hpp
/usr/include/armadillo_bits/op_sp_plus_meat.hpp
/usr/include/armadillo_bits/op_sqrtmat_bones.hpp
/usr/include/armadillo_bits/op_sqrtmat_meat.hpp
/usr/include/armadillo_bits/op_stddev_bones.hpp
/usr/include/armadillo_bits/op_stddev_meat.hpp
/usr/include/armadillo_bits/op_strans_bones.hpp
/usr/include/armadillo_bits/op_strans_meat.hpp
/usr/include/armadillo_bits/op_sum_bones.hpp
/usr/include/armadillo_bits/op_sum_meat.hpp
/usr/include/armadillo_bits/op_symmat_bones.hpp
/usr/include/armadillo_bits/op_symmat_meat.hpp
/usr/include/armadillo_bits/op_toeplitz_bones.hpp
/usr/include/armadillo_bits/op_toeplitz_meat.hpp
/usr/include/armadillo_bits/op_trimat_bones.hpp
/usr/include/armadillo_bits/op_trimat_meat.hpp
/usr/include/armadillo_bits/op_unique_bones.hpp
/usr/include/armadillo_bits/op_unique_meat.hpp
/usr/include/armadillo_bits/op_var_bones.hpp
/usr/include/armadillo_bits/op_var_meat.hpp
/usr/include/armadillo_bits/op_vectorise_bones.hpp
/usr/include/armadillo_bits/op_vectorise_meat.hpp
/usr/include/armadillo_bits/op_wishrnd_bones.hpp
/usr/include/armadillo_bits/op_wishrnd_meat.hpp
/usr/include/armadillo_bits/operator_cube_div.hpp
/usr/include/armadillo_bits/operator_cube_minus.hpp
/usr/include/armadillo_bits/operator_cube_plus.hpp
/usr/include/armadillo_bits/operator_cube_relational.hpp
/usr/include/armadillo_bits/operator_cube_schur.hpp
/usr/include/armadillo_bits/operator_cube_times.hpp
/usr/include/armadillo_bits/operator_div.hpp
/usr/include/armadillo_bits/operator_minus.hpp
/usr/include/armadillo_bits/operator_ostream.hpp
/usr/include/armadillo_bits/operator_plus.hpp
/usr/include/armadillo_bits/operator_relational.hpp
/usr/include/armadillo_bits/operator_schur.hpp
/usr/include/armadillo_bits/operator_times.hpp
/usr/include/armadillo_bits/podarray_bones.hpp
/usr/include/armadillo_bits/podarray_meat.hpp
/usr/include/armadillo_bits/promote_type.hpp
/usr/include/armadillo_bits/restrictors.hpp
/usr/include/armadillo_bits/running_stat_bones.hpp
/usr/include/armadillo_bits/running_stat_meat.hpp
/usr/include/armadillo_bits/running_stat_vec_bones.hpp
/usr/include/armadillo_bits/running_stat_vec_meat.hpp
/usr/include/armadillo_bits/sp_auxlib_bones.hpp
/usr/include/armadillo_bits/sp_auxlib_meat.hpp
/usr/include/armadillo_bits/span.hpp
/usr/include/armadillo_bits/spdiagview_bones.hpp
/usr/include/armadillo_bits/spdiagview_meat.hpp
/usr/include/armadillo_bits/spglue_elem_helper_bones.hpp
/usr/include/armadillo_bits/spglue_elem_helper_meat.hpp
/usr/include/armadillo_bits/spglue_join_bones.hpp
/usr/include/armadillo_bits/spglue_join_meat.hpp
/usr/include/armadillo_bits/spglue_kron_bones.hpp
/usr/include/armadillo_bits/spglue_kron_meat.hpp
/usr/include/armadillo_bits/spglue_max_bones.hpp
/usr/include/armadillo_bits/spglue_max_meat.hpp
/usr/include/armadillo_bits/spglue_merge_bones.hpp
/usr/include/armadillo_bits/spglue_merge_meat.hpp
/usr/include/armadillo_bits/spglue_min_bones.hpp
/usr/include/armadillo_bits/spglue_min_meat.hpp
/usr/include/armadillo_bits/spglue_minus_bones.hpp
/usr/include/armadillo_bits/spglue_minus_meat.hpp
/usr/include/armadillo_bits/spglue_plus_bones.hpp
/usr/include/armadillo_bits/spglue_plus_meat.hpp
/usr/include/armadillo_bits/spglue_schur_bones.hpp
/usr/include/armadillo_bits/spglue_schur_meat.hpp
/usr/include/armadillo_bits/spglue_times_bones.hpp
/usr/include/armadillo_bits/spglue_times_meat.hpp
/usr/include/armadillo_bits/spop_diagmat_bones.hpp
/usr/include/armadillo_bits/spop_diagmat_meat.hpp
/usr/include/armadillo_bits/spop_htrans_bones.hpp
/usr/include/armadillo_bits/spop_htrans_meat.hpp
/usr/include/armadillo_bits/spop_max_bones.hpp
/usr/include/armadillo_bits/spop_max_meat.hpp
/usr/include/armadillo_bits/spop_mean_bones.hpp
/usr/include/armadillo_bits/spop_mean_meat.hpp
/usr/include/armadillo_bits/spop_min_bones.hpp
/usr/include/armadillo_bits/spop_min_meat.hpp
/usr/include/armadillo_bits/spop_misc_bones.hpp
/usr/include/armadillo_bits/spop_misc_meat.hpp
/usr/include/armadillo_bits/spop_normalise_bones.hpp
/usr/include/armadillo_bits/spop_normalise_meat.hpp
/usr/include/armadillo_bits/spop_repmat_bones.hpp
/usr/include/armadillo_bits/spop_repmat_meat.hpp
/usr/include/armadillo_bits/spop_reverse_bones.hpp
/usr/include/armadillo_bits/spop_reverse_meat.hpp
/usr/include/armadillo_bits/spop_strans_bones.hpp
/usr/include/armadillo_bits/spop_strans_meat.hpp
/usr/include/armadillo_bits/spop_sum_bones.hpp
/usr/include/armadillo_bits/spop_sum_meat.hpp
/usr/include/armadillo_bits/spop_symmat_bones.hpp
/usr/include/armadillo_bits/spop_symmat_meat.hpp
/usr/include/armadillo_bits/spop_trimat_bones.hpp
/usr/include/armadillo_bits/spop_trimat_meat.hpp
/usr/include/armadillo_bits/spop_var_bones.hpp
/usr/include/armadillo_bits/spop_var_meat.hpp
/usr/include/armadillo_bits/spop_vectorise_bones.hpp
/usr/include/armadillo_bits/spop_vectorise_meat.hpp
/usr/include/armadillo_bits/strip.hpp
/usr/include/armadillo_bits/subview_bones.hpp
/usr/include/armadillo_bits/subview_cube_bones.hpp
/usr/include/armadillo_bits/subview_cube_each_bones.hpp
/usr/include/armadillo_bits/subview_cube_each_meat.hpp
/usr/include/armadillo_bits/subview_cube_meat.hpp
/usr/include/armadillo_bits/subview_cube_slices_bones.hpp
/usr/include/armadillo_bits/subview_cube_slices_meat.hpp
/usr/include/armadillo_bits/subview_each_bones.hpp
/usr/include/armadillo_bits/subview_each_meat.hpp
/usr/include/armadillo_bits/subview_elem1_bones.hpp
/usr/include/armadillo_bits/subview_elem1_meat.hpp
/usr/include/armadillo_bits/subview_elem2_bones.hpp
/usr/include/armadillo_bits/subview_elem2_meat.hpp
/usr/include/armadillo_bits/subview_field_bones.hpp
/usr/include/armadillo_bits/subview_field_meat.hpp
/usr/include/armadillo_bits/subview_meat.hpp
/usr/include/armadillo_bits/sympd_helper.hpp
/usr/include/armadillo_bits/traits.hpp
/usr/include/armadillo_bits/translate_arpack.hpp
/usr/include/armadillo_bits/translate_atlas.hpp
/usr/include/armadillo_bits/translate_blas.hpp
/usr/include/armadillo_bits/translate_lapack.hpp
/usr/include/armadillo_bits/translate_superlu.hpp
/usr/include/armadillo_bits/typedef_elem.hpp
/usr/include/armadillo_bits/typedef_elem_check.hpp
/usr/include/armadillo_bits/typedef_mat.hpp
/usr/include/armadillo_bits/typedef_mat_fixed.hpp
/usr/include/armadillo_bits/unwrap.hpp
/usr/include/armadillo_bits/unwrap_cube.hpp
/usr/include/armadillo_bits/unwrap_spmat.hpp
/usr/include/armadillo_bits/upgrade_val.hpp
/usr/include/armadillo_bits/wall_clock_bones.hpp
/usr/include/armadillo_bits/wall_clock_meat.hpp
/usr/include/armadillo_bits/xtrans_mat_bones.hpp
/usr/include/armadillo_bits/xtrans_mat_meat.hpp
/usr/include/armadillo_bits/xvec_htrans_bones.hpp
/usr/include/armadillo_bits/xvec_htrans_meat.hpp
/usr/lib64/libarmadillo.so
/usr/lib64/pkgconfig/armadillo.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libarmadillo.so.9
/usr/lib64/libarmadillo.so.9.600.4

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/armadillo/LICENSE.txt
