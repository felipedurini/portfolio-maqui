import os

def create_carousel_html(image_folder):
    carousel_html = f'''
<div id="carouselExampleAutoplaying{keyletter}" class="carousel slide" data-bs-ride="carousel" data-bs-interval="2000" data-bs-pause="hover" data-bs-wrap="true">
  <div class="carousel-inner">
'''
    active = True
    for index, image_file in enumerate(os.listdir(image_folder)):
        if image_file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            carousel_html += f'''
    <div class="carousel-item {'active' if active else ''}">
      <img src="{os.path.join('imgs/coper', image_file)}" class="d-block w-100" alt="..." />
      {'<div class="carousel-caption d-none d-md-block">' if active else ''}
      {'<h4>Coper</h4>'  if active else ''}
      {'<p>Realizado por Maqui y Compañia</p>'  if active else ''}
      {'</div>' if active else ''}
    </div>
'''
            active = False

    carousel_html += f'''
  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleAutoplaying{keyletter}" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleAutoplaying{keyletter}" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div>
'''

    return carousel_html





# Replace 'image_folder_path' with the path to your image folder.
image_folder_path = 'C:\\Users\\Lenovo\\Downloads\\portfolio-maqui\\imgs\\coper'
keyletter = 'AD'
carousel_code = create_carousel_html(image_folder_path)
print(carousel_code)
# py carousel_generator.py