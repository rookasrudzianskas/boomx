package global

import (
	"time"
)

var (
	Version               = "dev"
	Commit                = ""
	BuildTime             = "none"
	Debug                 = false
	ProfilingEnabled      = false
	StartupTimeout        = 5 * time.Minute
	ConfigFilename        = "boomx.yaml"
	ReplicateRegistryHost = "r8.im"
	ReplicateWebsiteHost  = "boomx.com"
	LabelNamespace        = "run.boomx."
)
