BUILD_DIR := build

# Remove all build outputs and intermediate files.
clean:
	@ rm -rf $(BUILD_DIR)
	@ rm -rf gen

## Compile and run the AST generator.
generate_ast:
	@$(MAKE) -f java/Makefile DIR=java PACKAGE=tool
	@java -cp build/java com.craftinginterpreters.tool.GenerateAst \
			java/com/craftinginterpreters/lox

# Compile the Java interpreter .java files to .class files.
.PHONY: jlox
jlox: generate_ast
	@$(MAKE) -f java/Makefile DIR=java PACKAGE=lox
