import cv2
from pyzbar.pyzbar import decode
import json


cap = cv2.VideoCapture(1)

print("Pressione 'q' para sair.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    decoded_objects = decode(frame)

    for obj in decoded_objects:

        data = obj.data.decode("utf-8")
        try:
            dados = json.loads(data)
        except json.JSONDecodeError:
            dados = {"QR inválido": data}


        (x, y, w, h) = obj.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 8)

        text = f"{dados}"
        cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)


        print("QR Detectado:", dados)


    cv2.imshow("Leitor QR - Pressione 'q' para sair", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()