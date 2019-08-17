{
  pkgsSrc ? <nixpkgs>,
  pkgs ? import pkgsSrc {},
}:

with pkgs;

stdenv.mkDerivation {
  name = "ymldb-dev-env";
  buildInputs = [
    gnumake
    python3
    python3Packages.poetry
  ];
  LD_LIBRARY_PATH = [ "${libusb1}/lib" ];
}
