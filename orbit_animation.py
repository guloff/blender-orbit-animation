import bpy
import math
import random

# Данный скрипт предназначен для запуска только внутри Blender
def clear_keyframes(obj):
    """Удаление существующих ключевых кадров."""
    if obj.animation_data:
        obj.animation_data_clear()

def calculate_orbit_position(center, radius, angle):
    """Вычисление новой позиции планеты на орбите."""
    x = center.x + radius * math.cos(angle)
    y = center.y + radius * math.sin(angle)
    z = center.z  # Орбиты в плоскости XY
    return (x, y, z)

def setup_orbits():
    """Настройка орбит и анимации."""
    sun_name = "Sun"
    total_frames = 250

    # Получение объекта Sun
    sun = bpy.data.objects.get(sun_name)
    if not sun:
        print(f"Объект с именем '{sun_name}' не найден.")
        return

    sun_location = sun.location

    # Получение всех объектов с именем, начинающимся на 'Planet'
    planet_objects = [obj for obj in bpy.data.objects if obj.name.startswith("Planet")]

    # Сортировка планет по удаленности от Sun
    planet_objects.sort(key=lambda obj: math.sqrt(
        (obj.location.x - sun_location.x) ** 2 +
        (obj.location.y - sun_location.y) ** 2 +
        (obj.location.z - sun_location.z) ** 2
    ))

    # Вычисление общего количества оборотов для ближайшей планеты
    max_orbits = 3.0  # Максимальное количество оборотов для ближайшей планеты
    min_orbits = 0.5  # Минимальное количество оборотов для самой дальней планеты

    # Вычисление интервала изменения скорости
    orbits_decrement = (max_orbits - min_orbits) / (len(planet_objects) - 1)

    planet_data = []

    for i, obj in enumerate(planet_objects):
        clear_keyframes(obj)
        radius = math.sqrt(
            (obj.location.x - sun_location.x) ** 2 +
            (obj.location.y - sun_location.y) ** 2 +
            (obj.location.z - sun_location.z) ** 2
        )
        # Количество оборотов рассчитывается на основе позиции планеты в списке
        orbits = max_orbits - i * orbits_decrement
        # Начальный угол на орбите - случайный для каждого объекта
        initial_angle = random.uniform(0, 2 * math.pi)
        planet_data.append({
            "name": obj.name,
            "radius": radius,
            "orbits": orbits,
            "initial_angle": initial_angle
        })
        print(f"{obj.name} - Радиус орбиты: {radius}, Оборотов: {orbits}, Начальный угол: {initial_angle}")

    # Установка фрейма 1
    bpy.context.scene.frame_set(1)

    # Добавление ключевых кадров для каждой планеты с учетом начального угла
    for planet in planet_data:
        obj = bpy.data.objects.get(planet["name"])
        if not obj:
            continue
        new_location = calculate_orbit_position(sun_location, planet["radius"], planet["initial_angle"])
        obj.location = new_location
        obj.keyframe_insert(data_path="location", frame=1)

    # Итерация по каждому кадру для анимации
    for frame in range(2, total_frames + 1):
        bpy.context.scene.frame_set(frame)
        for planet in planet_data:
            obj = bpy.data.objects.get(planet["name"])
            if not obj:
                continue
            radius = planet["radius"]
            total_orbits = planet["orbits"]
            total_angle = 2 * math.pi * total_orbits
            # Добавляем начальный угол к углу, вычисляемому по времени
            angle = planet["initial_angle"] + (total_angle / total_frames) * frame
            new_location = calculate_orbit_position(sun_location, radius, angle)
            obj.location = new_location
            obj.keyframe_insert(data_path="location", frame=frame)

    print("Анимация орбит успешно создана.")

# Запуск настройки орбит
setup_orbits()