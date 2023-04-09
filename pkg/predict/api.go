package predict

import "github.com/boomx/boomx/pkg/config"

type HelpResponse struct {
	Arguments map[string]*config.RunArgument `json:"arguments"`
}
