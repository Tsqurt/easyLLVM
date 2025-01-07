# easyLLVM
A user-friendly configurator for simplifying LLVM processing workflows, supporting both traditional workflow mode and atomic mode.

## Usage

Note: this feature is not implemented yet.

```bash
# easyLLVM is an adapter for compiler, you can use it, just like clang
easyLLVM -c input.c -o output.o
easyLLVM main.c -o main.elf

# the only difference is '-c' is omitted (default behavior)
# result is determined by whether the file contains 'main' function
easyLLVM input.c -o output.elf # OK, not executable
easyLLVM -c main.c -o main.o # OK, executable

# you can also use it as a project management tool
easyLLVM your_project.yaml

# to create a valid yaml file, you can use the following command
easyLLVM --init-project your_project.yaml
# Note: the default yaml need not to be modified if you add/remove files, to build an executable or some executables, but you can modify it at your will.

# to build an library, you may specify your API, and then build it
easyLLVM your_api.yaml

```
By default, easyLLVM will determine your files automatically (for exampe, which files contains 'main' function), and then build them.
If you have multiple files contains 'main' function, it is also OK, easyLLVM will build them all. However, BE CAREFUL FOR NAME CONFLICTS!!! Only the 'main' function is allowed to be defined in 
multiple files, otherwise, it will cause name conflicts.

However, all above can be overridden by your configuration, you can specify which is your files to be built, and specify the output file name, and how to build them. easyLLVM will follow your configuration to build your project.

Your global configuration is in `~/.easyLLVM/config.yaml`, you can modify it at your will. `easyLLVM --reset-global-config` will reset it. However, it's not recommended to modify it, as it may cause unexpected behavior.

For your project configuration, it is in your project directory, named `<your_project>.yaml`, you can modify it at your will.

You can also specify your leaf nodes configuration, as a part of your project. For example, if your file is `a.c`, `a.c.yaml` is the configuration for `a.c`.

We propose a new way to use LLVM, which is more flexible and powerful, as it can apply your configuration recursively, with leaf configuration overriding parent configuration.

To manage these configurations, you can use easyLLVMGUI, which is a GUI tool for managing your configurations.

Note: You are not supposed to build a file under a project independently, you must build the whole project to build a file for consistency (as a signal file won't inherit the configuration of its parent). However, you can specify a `main` function or specify some properties in the project root to build a certain file for debug purpose.

Projects may be nested, and the default behavior is the child project will override the parent project's configuration, so it's safe to import a parent project into a child project.

## Working Mode

There are two working modes: traditional workflow mode and atomic mode.

Traditional workflow mode is the traditional way to use LLVM, you may be familiar with it. If you want to use another project management tool, you may want to use this mode: just a simple command line, to read from a file and then output a file.

Atomic mode is a new mode, which is designed to be used in a project management tool. It's a new way to use LLVM, which is more flexible and powerful, as it can apply your configuration recursively, with leaf configuration overriding parent configuration.

### Traditional Workflow Mode

This mode is the traditional way to use LLVM, input a file, output a file, with customizable configuration for each process. For example, you can choose to compile the file using easyLLVM just like you compile it directly with `clang` or `clang++`. 

If not specified as a project, this mode is the default mode of easyLLVM, as you can see, it's something just as simple as a wrapper of `clang`. Now you can use it as you like, to integrate into your project, and using it as a compiler adapter to replace `clang` or `llvm` in your project, to avoid the hassle of configuring `clang` or `llvm` in your project.

There is only one exception, if your file contains `main` function, your output file will be a executable file, which is the default behavior of `clang`, otherwise, it will be a `.o` file. This rule save you from manually choosing `-c` option for each file(-c is then omitted), is this good or bad? As it may break your traditional workflow which breaks the consistency of your project from `gcc` or `clang`, but it's a good thing to have. Anyway, you can always choose `no intelligent-c` mode to disable this feature. Or you can use some configuration to disable this feature for a specific file.

### Atomic Mode

Generally, easyLLVM provide two types of atomic mode:

1. **natural atoms** a natural atom is a **compilation unit**, which is a file that can be compiled independently. 

2. **logical atoms** Initialize a project, input multiple files, split these files into **logical atoms** if you like - generally speaking, each file contains only one function or global object, and then build into a library through automated analysis of atomic dependencies.

Whether you use natural atoms or logical atoms, be free to choose the mode you like. The only difference is that natural atoms will be seen as a free part, without any dependency analysis. So if you want to carry out some dependency analysis and remove some unused parts automatically, you must use logical atoms, especially when you want to build a library - you can ensure that the library is minimal and never emit any unused parts (and you can remove symbols' name in default). If you use natural atoms, you can only remove unused parts manually or specify some options/passes to remove them.
