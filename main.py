class PlanPago:
    """Clase para gestionar un plan de pago individual"""
    
    def __init__(self, nombre, monto_total, cantidad_cuotas, tasa_interes=0):
        self.nombre = nombre
        self.monto_total = monto_total
        self.cantidad_cuotas = cantidad_cuotas
        self.tasa_interes = tasa_interes
        self.cuotas = []
        self.generar_cuotas()
    
    def generar_cuotas(self):
        """Genera las cuotas del plan de pago"""
        monto_interes = self.monto_total * (self.tasa_interes / 100)
        monto_total_con_interes = self.monto_total + monto_interes
        valor_cuota = monto_total_con_interes / self.cantidad_cuotas
        
        for i in range(1, self.cantidad_cuotas + 1):
            self.cuotas.append({
                'numero': i,
                'valor': round(valor_cuota, 2),
                'pagada': False
            })
    
    def pagar_cuota(self, numero_cuota):
        """Marca una cuota como pagada"""
        if 0 < numero_cuota <= len(self.cuotas):
            self.cuotas[numero_cuota - 1]['pagada'] = True
            return True
        return False
    
    def obtener_resumen(self):
        """Retorna un resumen del plan de pago"""
        pagadas = sum(1 for c in self.cuotas if c['pagada'])
        return {
            'nombre': self.nombre,
            'monto_original': self.monto_total,
            'total_cuotas': self.cantidad_cuotas,
            'cuotas_pagadas': pagadas,
            'cuotas_pendientes': self.cantidad_cuotas - pagadas,
            'valor_cuota': self.cuotas[0]['valor'] if self.cuotas else 0
        }


class GestorPlanes:
    """Clase principal para gestionar múltiples planes de pago"""
    
    def __init__(self):
        self.planes = []
    
    def crear_plan(self, nombre, monto, cuotas, interes=0):
        """Crea un nuevo plan de pago"""
        plan = PlanPago(nombre, monto, cuotas, interes)
        self.planes.append(plan)
        return plan
    
    def listar_planes(self):
        """Lista todos los planes de pago"""
        return [plan.obtener_resumen() for plan in self.planes]
    
    def obtener_plan(self, nombre):
        """Obtiene un plan específico por nombre"""
        for plan in self.planes:
            if plan.nombre == nombre:
                return plan
        return None


def main():
    gestor = GestorPlanes()
    
    while True:
        print("\nGestor de Planes de Pago")
        print("1. Crear un nuevo plan")
        print("2. Pagar una cuota")
        print("3. Listar planes")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            nombre = input("Nombre del plan: ")
            monto = float(input("Monto total: "))
            cuotas = int(input("Cantidad de cuotas: "))
            interes = float(input("Tasa de interés (0 si no aplica): "))
            gestor.crear_plan(nombre, monto, cuotas, interes)
            print("Plan creado exitosamente.")
        
        elif opcion == '2':
            nombre = input("Nombre del plan: ")
            plan = gestor.obtener_plan(nombre)
            if plan:
                numero_cuota = int(input("Número de cuota a pagar: "))
                if plan.pagar_cuota(numero_cuota):
                    print("Cuota pagada exitosamente.")
                else:
                    print("Número de cuota inválido.")
            else:
                print("Plan no encontrado.")
        
        elif opcion == '3':
            planes = gestor.listar_planes()
            for plan in planes:
                print(plan)
        
        elif opcion == '4':
            print("Saliendo del gestor.")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()