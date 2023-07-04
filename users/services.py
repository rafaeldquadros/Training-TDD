from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import create_access_tokens

from .model import UsersModel
from .exceptions import (
    UsersAlreadyExistisExcpetion,
    UserEmailOrPasswordInvalidExcpetion,
)


class UsersService:
    def create(self, **kwargs):
        user = UsersModel.find_user_email(kwargs["email"])
        if user:
            raise UsersAlreadyExistisExcpetion(
                "Já existe um usuario cadastrado com este email: {}".format(
                    kwargs["email"]
                )
            )

        new_user = UsersModel(**kwargs)
        new_user.save()
        return new_user.as_dict()

    def login(self, **kwargs):
        user = UsersModel.find_user_email(kwargs["email"])
        if user and pbkdf2_sha256.verify(kwargs["password"], user.password):
            token = create_access_tokens(identity=user.id)
            return {"access_token": token}

        raise UserEmailOrPasswordInvalidExcpetion("Usuário ou senha invalidos")
