package image

import (
	"encoding/json"
	"fmt"

	"github.com/boomx/boomx/pkg/config"
	"github.com/boomx/boomx/pkg/docker"
	"github.com/boomx/boomx/pkg/global"
)

func GetConfig(imageName string) (*config.Config, error) {
	image, err := docker.ImageInspect(imageName)
	if err != nil {
		return nil, fmt.Errorf("Failed to inspect %s: %w", imageName, err)
	}
	configString := image.Config.Labels[global.LabelNamespace+"config"]
	if configString == "" {
		// Deprecated. Remove for 1.0.
		configString = image.Config.Labels["org.cogmodel.config"]
	}
	if configString == "" {
		return nil, fmt.Errorf("Image %s does not appear to be a BoomX model", imageName)
	}
	conf := new(config.Config)
	if err := json.Unmarshal([]byte(configString), conf); err != nil {
		return nil, fmt.Errorf("Failed to parse config from %s: %w", imageName, err)
	}
	return conf, nil
}
