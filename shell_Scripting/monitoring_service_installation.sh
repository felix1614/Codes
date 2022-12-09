echo "Theiox monitoringService_service"
	    mkdir -p /monitoringService/tar/
	    mkdir -p /monitoringService/untar/

	    echo "Downloading Services from artifactory ..."
	    # recharge_pps
	    wget artifactory.elmeasure.com/products/theiox/$Downloadversion/monitoringService.tar.gz -O /monitoringService/tar/monitoringService.tar.gz
	    mv monitoringService.tar.gz /monitoringService/tar/.

	    echo "Downloading monitoringService from artifactory"
	    cd /monitoringService/tar/
	    echo "untar recharge_pps"
	    tar xzvf /monitoringService/tar/monitoringService.tar.gz -C /monitoringService/untar/
	    echo "moving recharge_pps"
	    rsync -r /monitoringService/untar/* /monitoringService/
	    cd /monitoringService/
	    chmod a+rwx ./*
	    mv /monitoringService/monitoringService/*.service /etc/systemd/system/.

	    echo "monitoringService enabled"
	    sudo systemctl enable recharge.service
	    echo "Daemon-reload"
	    sudo systemctl daemon-reload
	    echo "monitoringService started"
	    sudo systemctl start recharge.service
	    echo "monitoringService started"

	    echo "Installed monitoringService."