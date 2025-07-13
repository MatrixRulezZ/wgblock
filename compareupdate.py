import os

def open_domain_ip_list():
    #пачка ипшников после прохода скрипта
    input_ips = open('domain-ip-resolve')
    list_input_ips = [valin.strip() for valin in input_ips]
    input_ips.close()

    #print(list_input_ips)

    #пачка ипшников которые уже есть
    output_ips=open('output_ips.txt')
    list_output_ips = [valout.strip() for valout in output_ips]
    output_ips.close()

    #print(list_output_ips)

    #сравниваем полученный список ипшников с имеющимся списком
    delta = list(set(list_input_ips) - set(list_output_ips))

    #print(delta)

    #ипшникики, отсуствующие в гитхабе, но имеющиеся после прохода - добавляем в дополняемый
    list_output_ips.extend(delta)

    #перезаписываем дополняемый со списком новых ипшников
    output_ips = open('output_ips.txt','w+')
    for val in list_output_ips:
        output_ips.write(val+'\n')
    output_ips.close()

if __name__ == '__main__':
    open_domain_ip_list()
