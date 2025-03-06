from pydantic import BaseModel, EmailStr

class LoginRequest(BaseModel):
    username: str
    password: str

class RegisterRequest(BaseModel):
    username: str
    matricula: str
    email: EmailStr
    password: str

class RegisterResponse(BaseModel):
    id: int
    username: str
    matricula: str
    email: EmailStr

    class Config:
        from_attributes = True