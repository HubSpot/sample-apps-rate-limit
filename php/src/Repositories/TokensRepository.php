<?php

namespace Repositories;

use Helpers\RedisHelper;

class TokensRepository
{
    public const TOKEN_KEY = 'token';

    public static function getToken(): ?array
    {
        $token = RedisHelper::getClient()->get(static::TOKEN_KEY);

        if (empty($token)) {
            return null;
        }

        return (array) json_decode($token);
    }

    public static function save(array $token)
    {
        RedisHelper::getClient()->set(static::TOKEN_KEY, json_encode($token));
    }

    public static function remove()
    {
        RedisHelper::getClient()->del(static::TOKEN_KEY);
    }
}
