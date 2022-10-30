{ lib , pkgs, buildPythonApplication, aiosqlite, websockets, fetchFromGitHub }:
buildPythonApplication rec {
  pname = "ws-scrapper";
  version = "0.1";
  doCheck = false;
  src = ./. ;
  propagatedBuildInputs = [ aiosqlite websockets ];
}
