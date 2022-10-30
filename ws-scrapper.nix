{ lib , pkgs, buildPythonApplication, websockets, fetchFromGitHub }:
buildPythonApplication rec {
  pname = "ws-scrapper";
  version = "1.0";
  doCheck = false;
  src = ./. ;
  propagatedBuildInputs = [ websockets ];
}
