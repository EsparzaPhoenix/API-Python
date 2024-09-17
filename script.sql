CREATE TABLE Usuario (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nome NVARCHAR(100) NOT NULL,
    email NVARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE Curriculo (
    id INT IDENTITY(1,1) PRIMARY KEY,
    usuario_id INT NOT NULL,
    educacao NVARCHAR(255),
    experiencia NVARCHAR(MAX),
    habilidades NVARCHAR(255),
    FOREIGN KEY (usuario_id) REFERENCES Usuario(id)
);