<?php
use Repositories\TokensRepository;

TokensRepository::remove();

sleep(1);

header('Location: /');
