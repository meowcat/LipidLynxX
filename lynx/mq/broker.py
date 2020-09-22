# -*- coding: utf-8 -*-
#
# Copyright (C) 2016-2020  SysMedOs_team @ AG Bioanalytik, University of Leipzig:
#
# LipidLynxX is using GPL V3 License
#
# Please cite our publication in an appropriate form.
#   LipidLynxX preprint on bioRxiv.org
#   Zhixu Ni, Maria Fedorova.
#   "LipidLynxX: a data transfer hub to support integration of large scale lipidomics datasets"
#   DOI: 10.1101/2020.04.09.033894
#
# For more info please contact:
#     Developer Zhixu Ni zhixu.ni@uni-leipzig.de

import zmq

from lynx.models.defaults import default_zmq_worker_port, default_zmq_client_port


def default_broker():
    # Prepare our context and sockets
    context = zmq.Context()
    client = context.socket(zmq.ROUTER)
    worker = context.socket(zmq.DEALER)
    client.bind(f"tcp://*:{default_zmq_client_port}")
    worker.bind(f"tcp://*:{default_zmq_worker_port}")

    # Initialize poll set
    poller = zmq.Poller()
    poller.register(client, zmq.POLLIN)
    poller.register(worker, zmq.POLLIN)

    # Switch messages between sockets
    print("ZMQ Broker started.")
    while True:
        socks = dict(poller.poll())

        if socks.get(client) == zmq.POLLIN:
            message = client.recv_multipart()
            worker.send_multipart(message)

        if socks.get(worker) == zmq.POLLIN:
            message = worker.recv_multipart()
            client.send_multipart(message)
