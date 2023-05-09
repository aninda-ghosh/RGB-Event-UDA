#! TASK BACKEND
Sequential(
	(0): Sequential(
		(0): BasicBlock(
			(conv1): Conv2d(128, 256, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), bias=False)
			(bn1): BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
			(relu): ReLU(inplace=True)
			(conv2): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
			(bn2): BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
			(downsample): Sequential(
				(0): Conv2d(128, 256, kernel_size=(1, 1), stride=(2, 2), bias=False)
				(1): BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
			)
		)
		(1): BasicBlock(
			(conv1): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
			(bn1): BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
			(relu): ReLU(inplace=True)
			(conv2): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
			(bn2): BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		)
	)
	(1): Sequential(
		(0): BasicBlock(
			(conv1): Conv2d(256, 512, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), bias=False)
			(bn1): BatchNorm2d(512, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
			(relu): ReLU(inplace=True)
			(conv2): Conv2d(512, 512, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
			(bn2): BatchNorm2d(512, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
			(downsample): Sequential(
				(0): Conv2d(256, 512, kernel_size=(1, 1), stride=(2, 2), bias=False)
				(1): BatchNorm2d(512, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
			)
		)
		(1): BasicBlock(
			(conv1): Conv2d(512, 512, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
			(bn1): BatchNorm2d(512, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
			(relu): ReLU(inplace=True)
			(conv2): Conv2d(512, 512, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
			(bn2): BatchNorm2d(512, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		)
	)
	(2): AdaptiveAvgPool2d(output_size=(1, 1))
	(3): Flatten(start_dim=1, end_dim=-1)
	(4): Linear(in_features=512, out_features=101, bias=True)
)