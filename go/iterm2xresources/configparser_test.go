package iterm2xresources

import "testing"

func TestName(t *testing.T) {
	if Name != "hey" {
		t.Error(`Name = false`)
	}
}
