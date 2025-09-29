
Este archivo es solo un resumen, no modifiques nada hasta que te confirme.

Analiza a profundidad esta carpeta @stable-diffusion-webui_Warcklian/ es un proyecto previo, pero nos servira como docuementacion, por lo que sus archivos no se usaran para produccion, si se requiere alguno de sus archivos o parte de su codigo, debera copiarse a la carpeta correspondiente de nuestro nuevo proyecto.

Te explico brevemente en que consiste el proyecto anterior y que quiero en el nuevo.

El anterior ejecuta el webui de stablediffussion en modo grafico y le implemente varias cosas adicionales las principales, genracion masiva de imagenes usando json y png de muestra y genereacion masiva genetica, para diversidad real, en lo sucesivo las llamare masivo y genetico.
Ambos crean imagenes tipo pasaporte siguiendo las normas y especificaciones SAIME.

Pero el sistema se volvio muy pesado y lento lo cual dificulta seguir con su desarrollo.



Lo que necesito en el nuevo proyecto es lo siguiente:

Ejecutar una instancia de stablediffussion limpia tal como esta en el repositorio de Github pero sin modo grafico ya que solo la usaremos para conectarnos via API.

Vamos a crear un panel web similar al que esta implementado en el proyecto anterior pero solo se usaran para envirse cia Api a la webui, tendremos:

1. El selector de modelo a usar, tal como lo tiene webui, con combobox etc, se envia por API.

2. La pestaña genetica con todas sus funcionalidades, comboboxes, que generaran los json con toda la informacion y configuraciones necesarias, para generar los json png csv, para la creacion de las imagenes se enviaran los datos necesarios para crear las imagenes en este caso los json se envia por API, para la genereacion masiva genetica, con la diversidad requerida, revisa bien los .md del proyecto original ahi esta todo especificado.

3. La pestaña para la generacion masiva pasaporte con toda su funcionalidad usara una carpeta donde ire colocando json y png para usarlo como base para crear mas imagenes con esos parametros pero creando diversads personas, es decir relativamente mismo promt pero con ligeros cambios tomados de la web nueva como cfg sacala ancho alto etc.

4. La ubicacion de las imagenes debe seguir la misma nomenclatura y ubicacion que se tiene en el proyecto original.