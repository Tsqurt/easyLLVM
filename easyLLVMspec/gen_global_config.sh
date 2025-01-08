rm -f template_easyLLVM.yaml
cat *.yaml > template_easyLLVM.ez
rm -f ~/.ez
ln -s ~/easyLLVM/easyLLVMspec/template_easyLLVM.ez ~/.ez