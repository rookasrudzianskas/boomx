package predict

import "github.com/boomx/cog/pkg/config"

type HelpResponse struct {
	Arguments map[string]*config.RunArgument `json:"arguments"`
}
