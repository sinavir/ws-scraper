{ pkgs ? import ./nix {} }:
pkgs.python310Packages.callPackage ./ws-scrapper.nix {
  aiosqlite = pkgs.python310Packages.aiosqlite.overrideAttrs (old:{
    propagatedBuildInputs = old.propagatedBuildInputs ++ 
      [ pkgs.python310Packages.typing-extensions ];
  });
}
