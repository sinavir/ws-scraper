{ pkgs ? import ./nix {} }:
pkgs.python310Packages.callPackage ./ws-scrapper.nix {}
