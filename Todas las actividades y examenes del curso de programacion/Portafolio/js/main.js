/* ==========================================================================
   1. NAVBAR PEGAJOSA (Sticky Navbar)
   Al bajar mas de 20px, la barra de navegación cambia de estilo
   ========================================================================== */
var navbar = document.querySelector(".navbar");

window.onscroll = () => {
    // Si el scroll vertical es mayor a 20, añade la clase "sticky", si no, la quita
    this.scrollY > 20 ? navbar.classList.add("sticky") : navbar.classList.remove("sticky");
}

/* ==========================================================================
   2. MENU MOVIL (Toggle)
   Controla la apertura y cierre del menu hamburguesa en celulares
   ========================================================================== */
const navMenu = document.querySelector(".menu");
const navToggle = document.querySelector(".menu-btn");

if(navToggle) {
    navToggle.addEventListener("click", () => {
        // Al hacer clic en el boton, pone o quita la clase "active" al menu
        navMenu.classList.toggle("active");
    })
}

// Cierra el menu automaticamente cuando haces clic en cualquier enlace interno
const navLink = document.querySelectorAll(".nav-link");

function linkAction() {
    const navMenu = document.querySelector(".menu");
    navMenu.classList.remove("active");
}
navLink.forEach(n => n.addEventListener("click", linkAction));

/* ==========================================================================
   3. ENLACE ACTIVO AL HACER SCROLL
   Resalta en el menu la seccion, donde te encuentras actualmente
   ========================================================================== */
const Section = document.querySelectorAll('section[id]');

function scrollActive() {
    const scrollY = window.pageYOffset;
    Section.forEach(current => {
        const sectionHeight = current.offsetHeight;
        const sectionTop = current.offsetTop - 50;
        const sectionId = current.getAttribute('id');
        
        // Verifica si estas dentro del rango de la seccion
        if(scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
            document.querySelector('.links a[href*=' + sectionId + ']').classList.add('active');
        } else {
            document.querySelector('.links a[href*=' + sectionId + ']').classList.remove('active');
        }
    })
}
window.addEventListener('scroll', scrollActive);

/* ==========================================================================
   4. ANIMACION DE HABILIDADES (Skills)
   Hace que las barras de progreso crezcan cuando el usuario llega a esa seccion
   ========================================================================== */
const skills_wrap = document.querySelector(".about-skills");
const skills_bar = document.querySelectorAll(".progress-line");

window.addEventListener("scroll", () => {
    skillsEffect();
});

// Funcion que revisa si la seccion de Skills ya entro en la pantalla del usuario
function checkScroll(el) {
    let rect = el.getBoundingClientRect();
    if(window.innerHeight >= rect.top + el.offsetHeight) return true;
    return false;
}

// Aplica el ancho a las barras segun el atributo
function skillsEffect() {
    if(!checkScroll(skills_wrap)) return;
    skills_bar.forEach((skill) => (skill.style.width = skill.dataset.progress));
}

/* ==========================================================================
   5. FILTRO DEL PORTAFOLIO
   Filtra los proyectos (Diseño Web, Música, etc.) al hacer clic en los botones
   ========================================================================== */
const FilterContainer = document.querySelector(".portfolio-filter"),
      filterBtns = FilterContainer.children,
      totalFilterBtn = filterBtns.length,
      PortfolioItems = document.querySelectorAll(".portfolio-item"),
      totalportfolioItem = PortfolioItems.length;

for(let i=0; i < totalFilterBtn; i++) {
    filterBtns[i].addEventListener("click", function() {
        // Cambia el estado "activo" entre los botones de filtro
        FilterContainer.querySelector(".active").classList.remove("active");
        this.classList.add("active");

        const filterValue = this.getAttribute("data-filter");
        
        for(let k=0; k<totalportfolioItem; k++) {
            // Muestra u oculta los proyectos segun la categoria seleccionada
            if(filterValue === PortfolioItems[k].getAttribute("data-category")) {
                PortfolioItems[k].classList.remove("hide");
                PortfolioItems[k].classList.add("show");
            } else {
                PortfolioItems[k].classList.remove("show");
                PortfolioItems[k].classList.add("hide");
            }
            // Si el filtro es "all" (Todos), los muestra todos
            if(filterValue === "all") {
                PortfolioItems[k].classList.remove("hide");
                PortfolioItems[k].classList.add("show");
            }
        }
    })
}

/* ==========================================================================
   6. VISUALIZADOR DE IMAGENES
   Maneja la ventana emergente que muestra la foto en grande al hacer clic
   ========================================================================== */
const lightbox = document.querySelector(".lightbox"),
      lightboxImg = lightbox.querySelector(".lightbox-img"),
      lightboxClose = lightbox.querySelector(".lightbox-close"),
      lightboxText = lightbox.querySelector(".caption-text"),
      lightboxCounter = lightbox.querySelector(".caption-counter");

let itemIndex = 0;

for(let i=0; i<totalportfolioItem; i++) {
    PortfolioItems[i].addEventListener("click", function() {
        itemIndex = i;
        changeItem();
        toggleLightbox();
    })
}

// Funciones para pasar de imagen (Siguiente/Anterior)
function nextItem() {
    itemIndex == totalportfolioItem - 1 ? itemIndex = 0 : itemIndex++;
    changeItem();
}

function prevItem() {
    itemIndex == 0 ? itemIndex = totalportfolioItem - 1 : itemIndex--;
    changeItem();
}

// Abre o cierra la ventana emergente
function toggleLightbox() {
    lightbox.classList.toggle("open");
}

// Actualiza el contenido del Lightbox (Imagen, Titulo y Contador)
function changeItem() {
    imgSrc = PortfolioItems[itemIndex].querySelector(".portfolio-img img").getAttribute("src");
    lightboxImg.src = imgSrc;
    lightboxText.innerHTML = PortfolioItems[itemIndex].querySelector("h4").innerHTML;
    lightboxCounter.innerHTML = (itemIndex + 1) + " of " + totalportfolioItem;
}

// Cierra el Lightbox si haces clic en la "X" o fuera de la imagen
lightbox.addEventListener("click", function(event) {
    if(event.target === lightboxClose || event.target === lightbox) {
        toggleLightbox();
    }
})
