# easyLLVM Specification

This directory contains the specification for easyLLVM configuration system, which defines how easyLLVM configurations are structured and processed.

## Configuration Hierarchy

easyLLVM uses a hierarchical configuration system with three levels:

1. Global Configuration (`~/.ez`)
   - System-wide default settings
   - Not recommended to modify directly
   - Can be reset using `easyLLVM --reset-global-config`

2. Project Configuration (`<project_name>.ez`) 
   - Project-level settings
   - Overrides global configuration if specified
   - Defines project structure, build targets, and dependencies (if any)
   - Supports nested projects with child projects inheriting parent settings

3. Leaf Configuration (`<source_file>.ez`)
   - File-specific settings
   - Highest priority, overrides project and global settings
   - Controls compilation flags, optimization levels etc. for individual files

## Configuration Format

All configuration files use YAML format. The basic structure includes:

TODO: add example
