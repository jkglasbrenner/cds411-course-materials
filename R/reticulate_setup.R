if (Sys.getenv("RETICULATE_CONDA_INSTALLATION_PATH") != "") {
  reticulate::use_condaenv(
    condaenv = "cds411-dev",
    conda = Sys.getenv("RETICULATE_CONDA_INSTALLATION_PATH")
  )
}
