<?php

/**
 * @return null|mixed
 */
function getEnvOrException(string $name): string
{
    if (empty($_ENV[$name])) {
        throw new \Exception("Please specify {$name} in .env");
    }

    return $_ENV[$name];
}
