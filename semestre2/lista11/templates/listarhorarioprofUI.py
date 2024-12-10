import streamlit as st
import pandas as pd
from views import View

class ListarHorarioProfUI:
    def main():
        st.header("Horários Disponíveis")
        ListarHorarioUI.listar()

    def listar():
        horarios = View.horario_listar_disponiveis()
        if len(horarios) == 0:
            st.write("Nenhum horário disponível")
        else:
            # dic = []
            # for obj in horarios: 
            #     dic.append(obj.to_json())
            # df = pd.DataFrame(dic)
            # st.dataframe(df)
            
            dic = []
            for obj in horarios:
                for p in View.profissional_listar:
                    if p.id == st.session_state["profissional_id"]:
                        dic.append({
                            "id": obj.id,
                            "data": obj.data,
                            "confirmado": obj.confirmado,
                        })
            df = pd.DataFrame(dic)
            st.dataframe(df)