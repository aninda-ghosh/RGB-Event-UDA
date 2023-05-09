#! FRONT END SENSOR B
StyleEncoder(
    (conv_layers): Sequential(
		(0): Conv2d(2, 64, kernel_size=(7, 7), stride=(2, 2), padding=(3, 3), bias=False)
		(1): BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		(2): ReLU(inplace=True)
		(3): Sequential(
			(0): BasicBlock(
			(conv1): Conv2d(64, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
			(bn1): BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
			(relu): ReLU(inplace=True)
			(conv2): Conv2d(64, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
			(bn2): BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
			)
			(1): BasicBlock(
			(conv1): Conv2d(64, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
			(bn1): BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
			(relu): ReLU(inplace=True)
			(conv2): Conv2d(64, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
			(bn2): BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
			)
		)
		(4): BasicBlock(
			(conv1): Conv2d(64, 128, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), bias=False)
			(bn1): BatchNorm2d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
			(relu): ReLU(inplace=True)
			(conv2): Conv2d(128, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
			(bn2): BatchNorm2d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
			(downsample): Sequential(
			(0): Conv2d(64, 128, kernel_size=(1, 1), stride=(2, 2), bias=False)
			(1): BatchNorm2d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
			)
		)
	)
	(conv_share): BasicBlock(
		(conv1): Conv2d(128, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
		(bn1): BatchNorm2d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		(relu): ReLU(inplace=True)
		(conv2): Conv2d(128, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
		(bn2): BatchNorm2d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
	)
	(attribute_encoder): E_attr_concat(
		(fc_A): Sequential(
			(0): Linear(in_features=256, out_features=8, bias=True)
		)
		(fcVar_A): Sequential(
			(0): Linear(in_features=256, out_features=8, bias=True)
		)
		(conv_layers): Sequential(
			(0): ReflectionPad2d((1, 1, 1, 1))
			(1): Conv2d(2, 64, kernel_size=(4, 4), stride=(2, 2))
			(2): BasicBlock(
				(conv): Sequential(
					(0): InstanceNorm2d(64, eps=1e-05, momentum=0.1, affine=False, track_running_stats=False)
					(1): LeakyReLU(negative_slope=0.01)
					(2): Conv2d(64, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
					(3): InstanceNorm2d(64, eps=1e-05, momentum=0.1, affine=False, track_running_stats=False)
					(4): LeakyReLU(negative_slope=0.01)
					(5): Sequential(
						(0): Conv2d(64, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
						(1): AvgPool2d(kernel_size=2, stride=2, padding=0)
					)
				)
				(shortcut): Sequential(
					(0): AvgPool2d(kernel_size=2, stride=2, padding=0)
					(1): Conv2d(64, 128, kernel_size=(1, 1), stride=(1, 1))
				)
			)
			(3): BasicBlock(
				(conv): Sequential(
					(0): InstanceNorm2d(128, eps=1e-05, momentum=0.1, affine=False, track_running_stats=False)
					(1): LeakyReLU(negative_slope=0.01)
					(2): Conv2d(128, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
					(3): InstanceNorm2d(128, eps=1e-05, momentum=0.1, affine=False, track_running_stats=False)
					(4): LeakyReLU(negative_slope=0.01)
					(5): Sequential(
					(0): Conv2d(128, 192, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
					(1): AvgPool2d(kernel_size=2, stride=2, padding=0)
					)
				)
				(shortcut): Sequential(
					(0): AvgPool2d(kernel_size=2, stride=2, padding=0)
					(1): Conv2d(128, 192, kernel_size=(1, 1), stride=(1, 1))
				)
			)
			(4): BasicBlock(
				(conv): Sequential(
					(0): InstanceNorm2d(192, eps=1e-05, momentum=0.1, affine=False, track_running_stats=False)
					(1): LeakyReLU(negative_slope=0.01)
					(2): Conv2d(192, 192, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
					(3): InstanceNorm2d(192, eps=1e-05, momentum=0.1, affine=False, track_running_stats=False)
					(4): LeakyReLU(negative_slope=0.01)
					(5): Sequential(
					(0): Conv2d(192, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
					(1): AvgPool2d(kernel_size=2, stride=2, padding=0)
					)
				)
				(shortcut): Sequential(
					(0): AvgPool2d(kernel_size=2, stride=2, padding=0)
					(1): Conv2d(192, 256, kernel_size=(1, 1), stride=(1, 1))
				)
			)
			(5): LeakyReLU(negative_slope=0.01)
			(6): AdaptiveAvgPool2d(output_size=1)
		)
    )
)