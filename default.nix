{ pkgs ? import <nixpkgs> {} }:
pkgs.python310Packages.callPackage ./ws-scrapper.nix {}
