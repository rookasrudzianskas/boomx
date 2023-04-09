package main

import (
	"github.com/boomx/boomx/pkg/cli"
	"github.com/boomx/boomx/pkg/util/console"
)

func main() {
	cmd, err := cli.NewRootCommand()
	if err != nil {
		console.Fatalf("%f", err)
	}

	if err = cmd.Execute(); err != nil {
		console.Fatalf("%s", err)
	}
}
