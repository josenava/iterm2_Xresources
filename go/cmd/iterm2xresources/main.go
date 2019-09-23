package main

import (
	"flag"
	"fmt"

	"github.com/josenava/iterm2_Xresources/go/iterm2xresources"
)

func main() {
	input_file_path := flag.String("from", "/tmp/file.xml", "File containing iterm2 colors")
	output_file_path := flag.String("to", "/tmp/file.xml", "File containing Xresources colors")
	flag.Parse()

	fmt.Printf("config %s\n", iterm2xresources.Name)
	fmt.Printf("input_file_path: %s\n", *input_file_path)
	fmt.Printf("output_file_path: %s\n", *output_file_path)
}
