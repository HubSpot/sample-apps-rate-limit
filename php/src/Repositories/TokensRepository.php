<?php

namespace Repositories;

use Helpers\RedisHelper;

class TokensRepository
{
    public static function getToken(): ?array
    {
        $token = RedisHelper::getClient()->get('token');

        if (empty($token)) {
            return null;
        }

        return (array) json_decode($token);
    }

    public static function save(array $token)
    {
        RedisHelper::getClient()->set('token', json_encode($token));
    }
}
