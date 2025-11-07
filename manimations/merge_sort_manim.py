from manim import *

class MergeSortVisual(Scene):
    def construct(self):
        titulo = Text("Método de Ordenamiento por Mezcla (MergeSort)", font_size=36)
        titulo.to_edge(UP)
        self.play(Write(titulo))

        # Arreglo de ejemplo
        array = [38, 27, 43, 9, 3, 82, 10]
        
        # se crea grupo inicial
        group = self.create_array(array, color=WHITE)
        group.move_to(ORIGIN + UP * 2) 
        
        self.play(FadeIn(group, shift=DOWN*0.5))
        self.wait(1)

        # Comienza el proceso del merge   
        final_group = self.merge_sort_visual(array, group)
        
        # Pequeña animación de "éxito" al final
        self.play(final_group.animate.scale(1.1).set_color(GREEN_C), run_time=0.5)
        self.play(final_group.animate.scale(1/1.1), run_time=0.5)

        texto_final = Text("¡Arreglo ordenado!", color=GREEN).next_to(final_group, DOWN, buff=0.5)
        self.play(Write(texto_final))
        self.wait(6)

    def create_array(self, arr, color=BLUE):
        """
        Crea una representación visual de un arreglo con cajas redondeadas.
        """
        boxes = VGroup()
        for num in arr:
            #RoundedRectangle se usa para crear cajas más suaves-chill
            box = RoundedRectangle(
                corner_radius=0.1, 
                height=0.9, 
                width=0.9, 
                color=color, 
                fill_opacity=0.5, 
                stroke_width=2
            )
            text = Text(str(num), font_size=28)
            text.move_to(box.get_center())
            boxes.add(VGroup(box, text))
            
        # Ajustamos el espaciado
        boxes.arrange(RIGHT, buff=0.15)
        return boxes

    def merge_sort_visual(self, arr, group):
        """
        Visualiza recursivamente el proceso de MergeSort.
        """
        if len(arr) <= 1:
            # Caso base, se marca en verde porque ya está ordenado
            self.play(group.animate.set_color(GREEN), run_time=0.3)
            return group

        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        # --- DIVISIÓN ---
        
        # Crear subgrupos visuales
        left_group = self.create_array(left_arr, color=BLUE_C)
        right_group = self.create_array(right_arr, color=BLUE_C)

        # Guardamos la posición del padre ANTES de cualquier animación
        parent_center = group.get_center()

        # crea el grupo y los alinea debajo del padre
        VGroup(left_group, right_group).arrange(RIGHT, buff=0.5).move_to(parent_center + DOWN * 1.5)

        # Animación de división:
        #Desaparece el padre (FadeOut) y aparecen los hijos.
        self.play(
            FadeOut(group, shift=DOWN*0.5), # El padre se va
            FadeIn(left_group, shift=UP*0.5),  # Los hijos aparecen
            FadeIn(right_group, shift=UP*0.5),
            run_time=1.5
        )
        self.wait(0.5)

        #Recursión en los hijos: una vez que vuelven a aparecer están en verde.
        left_sorted_group = self.merge_sort_visual(left_arr, left_group)
        right_sorted_group = self.merge_sort_visual(right_arr, right_group)

        # 1. Crear el nuevo grupo fusionado (ya ordenado)
        merged_arr = sorted(arr) # arr es left_arr + right_arr
        merged_group = self.create_array(merged_arr, color=GREEN)
        
        # se posiciona donde estaba el padre original (parent_center)
        merged_group.move_to(parent_center)

        texto_mezcla = Text("Fusionando...", font_size=24, color=YELLOW).next_to(merged_group, UP, buff=0.3)

        # 2. Animar la fusión
        self.play(Write(texto_mezcla))
        
        # Los hijos (verdes) se mueven hacia la posición del padre
        self.play(
            left_sorted_group.animate.move_to(parent_center),
            right_sorted_group.animate.move_to(parent_center),
            run_time=1.5
        )
        
        # 3. Desaparecen los hijos y aparece el padre fusionado
        self.play(
            FadeOut(left_sorted_group),
            FadeOut(right_sorted_group),
            FadeIn(merged_group, shift=DOWN*0.5) # Aparece el grupo fusionado
        )
        self.play(FadeOut(texto_mezcla))
        self.wait(0.3)

        # Devuelve el grupo fusionado y ordenado
        return merged_group
    
    #este codigo lo pongo nomás para que me quede a mano la ejecución en la terminal, por las dudas...
    #manim -pql merge_sort_manim.py MergeSortVisual