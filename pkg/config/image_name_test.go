package config

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func TestDockerImageName(t *testing.T) {
	require.Equal(t, "boomx-foo", DockerImageName("/home/joe/foo"))
	require.Equal(t, "boomx-foo", DockerImageName("/home/joe/Foo"))
	require.Equal(t, "boomx-my-great-model", DockerImageName("/home/joe/my great model"))
	require.Equal(t, 30, len(DockerImageName("/home/joe/verylongverylongverylongverylongverylongverylongverylong")))
}
