class Titulo:
    def __init__(self):
        self.nombre = "Titulo"
        self.rol = "Desarrollador Full Stack"
        self.lenguajes = ["Python", "JavaScript", "Java", "SQL"]
        self.tecnologias = {
            "backend": ["Django", "Flask", "Node.js", "FastAPI"],
            "frontend": ["React", "Vue.js", "HTML5", "CSS3"],
            "database": ["PostgreSQL", "MySQL", "MongoDB"],
            "tools": ["Git", "Docker", "AWS", "Linux"]
        }
        
    def decir_hola(self):
        print("¡Gracias por visitar mi perfil!")
