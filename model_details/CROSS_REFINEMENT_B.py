#! CROSS REFINEMENT B
StyleRefinementNetwork(
	(noise_model): Sequential(
		(0): Conv2d(4, 16, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
		(1): BatchNorm2d(16, eps=1e-05, momentum=0.01, affine=True, track_running_stats=True)
		(2): LeakyReLU(negative_slope=0.01)
		(3): Conv2d(16, 8, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
		(4): BatchNorm2d(8, eps=1e-05, momentum=0.01, affine=True, track_running_stats=True)
		(5): LeakyReLU(negative_slope=0.01)
		(6): Conv2d(8, 2, kernel_size=(1, 1), stride=(1, 1), bias=False)
		(7): ReLU()
	)
	(norm_gradient_layer): NormGradient(
		(padding_layer): ReflectionPad2d((2, 2, 2, 2))
	)
	(sigmoid_layer): Sigmoid()
)

CrossDiscriminator(
	(model): Sequential(
		(0): LeakyReLUConv2d(
			(model): Sequential(
				(0): Conv2d(2, 64, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1))
				(1): LeakyReLU(negative_slope=0.01, inplace=True)
			)
		)
		(1): LeakyReLUConv2d(
			(model): Sequential(
				(0): Conv2d(64, 128, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1))
				(1): LeakyReLU(negative_slope=0.01, inplace=True)
			)
		)
		(2): LeakyReLUConv2d(
			(model): Sequential(
				(0): Conv2d(128, 256, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1))
				(1): LeakyReLU(negative_slope=0.01, inplace=True)
			)
		)
		(3): LeakyReLUConv2d(
			(model): Sequential(
				(0): Conv2d(256, 512, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1))
				(1): LeakyReLU(negative_slope=0.01, inplace=True)
			)
		)
		(4): LeakyReLUConv2d(
			(model): Sequential(
				(0): Conv2d(512, 1024, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1))
				(1): LeakyReLU(negative_slope=0.01, inplace=True)
			)
		)
		(5): LeakyReLUConv2d(
			(model): Sequential(
				(0): Conv2d(1024, 2048, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1))
				(1): LeakyReLU(negative_slope=0.01, inplace=True)
			)
		)
		(6): Conv2d(2048, 1, kernel_size=(1, 1), stride=(1, 1))
	)
)