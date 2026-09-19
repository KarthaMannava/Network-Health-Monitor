<h1 align="center">📡 Ping Monitor CLI</h1>
<p align="center">
  🇺🇸 <a href="README.md"><b>English</b></a> |
  🇪🇸 <b>Español</b>
</p>
<h3 align="center">Monitor simple de conectividad de red en tiempo real escrito en Python.</h3>

Envía un ping por segundo a `8.8.8.8` y muestra:

* Latencia (ms)
* Detección de timeout de paquetes
* Promedio acumulado
* Latencia mínima
* Latencia máxima
* Total de pings exitosos
* Timestamp por solicitud

Diseñado para diagnósticos rápidos desde la terminal en Windows, Linux o WSL.

---

## ✨ Características

* Multiplataforma (Windows / Linux)
* Interfaz de terminal limpia
* Salida con colores ANSI
* Detección automática de timeout
* Estadísticas acumuladas:

  * `AVG`
  * `MIN`
  * `MAX`
  * Conteo de paquetes
* Monitoreo con intervalo de 1 segundo

---

## 🖥️ Ejemplo de Salida

<img width="902" height="508" alt="image" src="https://github.com/user-attachments/assets/323193df-8ac2-4b76-8f5d-346b73f96481" />

---

## 🧠 Cómo Funciona

* Usa `subprocess.run()` para ejecutar el comando `ping` del sistema.
* Selecciona automáticamente:

  * `-n 1 -w 10000` en Windows
  * `-c 1 -W 10` en Linux
* Extrae la latencia usando regex:

  ```
  time=8.32 ms
  ```
* Mantiene estadísticas en vivo en memoria.

Pensalo como un pequeño monitor de latidos de red corriendo en tu terminal.

---

## 📦 Requisitos

* Python 3.8+
* Comando `ping` del sistema disponible en el PATH

No requiere dependencias externas.

---

## 🚀 Uso

Cloná (`git clone https://github.com/URDev4ever/Ping-Monitor.git`) o descargá el script, luego:

```bash
python ping_monitor.py
```

> o `cd Ping-Monitor` primero si lo clonaste

Detener con:

```
CTRL + C
```

---

## 🔧 Personalización

Si querés cambiar el objetivo:

```python
command = ["ping", "-c", "1", "-W", "10", "8.8.8.8"]
```

Reemplazá `8.8.8.8` por:

* Tu router (ej. `192.168.0.1`)
* Cloudflare (`1.1.1.1`)
* Un host específico que quieras monitorear

---

## 📊 Métricas Explicadas

| Métrica | Significado                    |
| ------- | ------------------------------ |
| ms      | Latencia actual del ping       |
| AVG     | Latencia promedio desde inicio |
| MIN     | Latencia más baja registrada   |
| MAX     | Latencia más alta registrada   |
| Count   | Respuestas exitosas de ping    |

---

## 🛠 Casos de Uso

* Monitorear Wi-Fi inestable
* Detectar pérdida de paquetes
* Medir fluctuaciones de latencia
* Debuggear networking en WSL
* Alternativa liviana a herramientas como `mtr`

---

## ⚠️ Notas

* Esta herramienta fue probada *ÚNICAMENTE* en **Kali Linux (WSL)**; si encontrás bugs en otras distribuciones, avisame.
* No calcula el porcentaje de packet loss.
* Depende del binario `ping` del sistema.
* Los colores ANSI pueden no mostrarse correctamente en algunas terminales antiguas de Windows.

---

Hecho con <3 por URDev.
