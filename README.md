# easyLLVM
A user-friendly configurator for simplifying LLVM processing workflows, supporting both traditional workflow mode and atomic mode.

## Usage

### Traditional Workflow Mode

This mode is the traditional way to use LLVM, input a file, output a file, with customizable configuration for each process. For example, you can choose to compile the file using easyLLVM just like you compile it directly with `clang` or `clang++`. 

If not specified as a project, this mode is the default mode of easyLLVM, as you can see, it's something just as simple as a wrapper of `clang`. Now you can use it as you like, to integrate into your project, and using it as a compiler adapter to replace `clang` or `llvm` in your project, to avoid the hassle of configuring `clang` or `llvm` in your project.

There is only one exception, if your file contains `main` function, your output file will be a executable file, which is the default behavior of `clang`. This rule save you from manually choosing `-c` option for each file, is this good or bad? As it may break your traditional workflow which breaks the consistency of your project from `gcc` or `clang`, but it's a good thing to have. Anyway, you can always choose `no intelligent-c` mode to disable this feature. Or you can use some configuration to d.

### Atomic Mode

Generally, easyLLVM provide two types of atomic mode:

1. **natural atoms** a natural atom is a **compilation unit**, which is a file that can be compiled independently. 

2. **logical atoms** Initialize a project, input multiple files, split these files into **logical atoms** if you like - generally speaking, each file contains only one function or global object, and then build into a library through automated analysis of atomic dependencies.

Whether you use natural atoms or logical atoms, be free to choose the mode you like. The only difference is that natural atoms will be seen as a free part, without any dependency analysis. So if you want to carry out some dependency analysis and remove some unused parts automatically, you must use logical atoms, especially when you want to build a library - you can ensure that the library is minimal and never emit any unused parts (and you can remove symbols' name in default). If you use natural atoms, you can only remove unused parts manually or specify some options/passes to remove them.

