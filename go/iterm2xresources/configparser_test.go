package iterm2xresources

import "testing"

func TestName(t *testing.T) {
	config, err := ParseConfig("./sample_data.xml")
	if err != nil {
		t.Fatal(err)
	}
	if config != "hey" {
		t.Error(`Name is different = false`)
	}
}
