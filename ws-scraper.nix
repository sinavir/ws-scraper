{ lib , pkgs, buildPythonApplication, aiosqlite, websockets, fetchFromGitHub }:
buildPythonApplication rec {
  pname = "ws-scraper";
  version = "0.1";
  doCheck = false;
  src = ./. ;
  propagatedBuildInputs = builtins.trace "${aiosqlite}" [ aiosqlite websockets ];
}
