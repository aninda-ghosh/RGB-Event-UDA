#! DISCRIMINATOR
ContentDiscriminator(
	(model): Sequential(
		(0): LeakyReLUConv2d(
			(model): Sequential(
				(0): Conv2d(128, 128, kernel_size=(7, 7), stride=(2, 2), padding=(1, 1))
				(1): InstanceNorm2d(128, eps=1e-05, momentum=0.1, affine=False, track_running_stats=False)
				(2): LeakyReLU(negative_slope=0.01, inplace=True)
			)
		)
		(1): LeakyReLUConv2d(
			(model): Sequential(
				(0): Conv2d(128, 128, kernel_size=(7, 7), stride=(2, 2), padding=(1, 1))
				(1): InstanceNorm2d(128, eps=1e-05, momentum=0.1, affine=False, track_running_stats=False)
				(2): LeakyReLU(negative_slope=0.01, inplace=True)
			)
		)
		(2): LeakyReLUConv2d(
			(model): Sequential(
				(0): Conv2d(128, 128, kernel_size=(7, 7), stride=(1, 1), padding=(1, 1))
				(1): InstanceNorm2d(128, eps=1e-05, momentum=0.1, affine=False, track_running_stats=False)
				(2): LeakyReLU(negative_slope=0.01, inplace=True)
			)
		)
		(3): LeakyReLUConv2d(
			(model): Sequential(
				(0): Conv2d(128, 128, kernel_size=(4, 4), stride=(1, 1))
				(1): LeakyReLU(negative_slope=0.01, inplace=True)
			)
		)
		(4): Conv2d(128, 1, kernel_size=(1, 1), stride=(1, 1))
  	)
)