{ lib , pkgs, buildPythonApplication, websockets, fetchFromGitHub }:
buildPythonApplication rec {
  pname = "kfet-scrapper";
  version = "1.0";
  doCheck = false;
  src = ./. ;
  propagatedBuildInputs = [ websockets ];
}
