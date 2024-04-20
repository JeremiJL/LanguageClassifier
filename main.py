from network import Network, Perceptron

network = Network("merged_observations", 0.01)

print(network.accuracy)
result = network.classify("Zanieczyszczenie powietrza w dużych miastach Polski osiągnęło alarmujące poziomy, co stanowi poważne zagrożenie dla zdrowia publicznego. Eksperci apelują o podjęcie natychmiastowych działań w celu poprawy jakości powietrza i ochrony mieszkańców przed szkodliwymi skutkami zanieczyszczeń.")



print(result)
