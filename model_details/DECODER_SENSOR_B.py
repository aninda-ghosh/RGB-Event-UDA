DECODER SENSOR B
StyleDecoder(
	(decoder_scale_1): Sequential(
		(0): INSResBlock(
			(model): Sequential(
				(0): Conv2d(138, 138, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
				(1): InstanceNorm2d(138, eps=1e-05, momentum=0.1, affine=False, track_running_stats=False)
				(2): ReLU(inplace=True)
				(3): Conv2d(138, 138, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
				(4): InstanceNorm2d(138, eps=1e-05, momentum=0.1, affine=False, track_running_stats=False)
			)
		)
		(1): INSResBlock(
			(model): Sequential(
				(0): Conv2d(138, 138, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
				(1): InstanceNorm2d(138, eps=1e-05, momentum=0.1, affine=False, track_running_stats=False)
				(2): ReLU(inplace=True)
				(3): Conv2d(138, 138, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
				(4): InstanceNorm2d(138, eps=1e-05, momentum=0.1, affine=False, track_running_stats=False)
			)
		)
		(2): INSResBlock(
			(model): Sequential(
				(0): Conv2d(138, 138, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
				(1): InstanceNorm2d(138, eps=1e-05, momentum=0.1, affine=False, track_running_stats=False)
				(2): ReLU(inplace=True)
				(3): Conv2d(138, 138, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
				(4): InstanceNorm2d(138, eps=1e-05, momentum=0.1, affine=False, track_running_stats=False)
			)
		)
	)
	(decoder_scale_2): Sequential(
		(0): InterpolationLayer()
		(1): ReLUINSConv2d(
			(model): Sequential(
				(0): Conv2d(146, 73, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
				(1): InstanceNorm2d(73, eps=1e-05, momentum=0.1, affine=False, track_running_stats=False)
				(2): ReLU(inplace=True)
			)
		)
	)
	(decoder_scale_3): Sequential(
		(0): InterpolationLayer()
		(1): ReLUINSConv2d(
			(model): Sequential(
				(0): Conv2d(81, 40, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
				(1): InstanceNorm2d(40, eps=1e-05, momentum=0.1, affine=False, track_running_stats=False)
				(2): ReLU(inplace=True)
			)
		)
	)
	(decoder_scale_4): Sequential(
		(0): Conv2d(48, 2, kernel_size=(1, 1), stride=(1, 1))
	)
)