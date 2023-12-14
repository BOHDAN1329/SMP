import abc
from collections import Counter
from matplotlib import pyplot as plt
from utility.FileProcessor import CsvProcessor as csv_processor
from consumer import Consumer


class ConsumerService(abc.ABC):

    @abc.abstractmethod
    def __init__(self):
        self._consumers = []

    @abc.abstractmethod
    def get_states(self):
        pass

    @abc.abstractmethod
    def create_chart(self, chart_type, has_to_be_downloaded, max_quantity=10):
        pass


class ConsumerServiceImpl(ConsumerService):

    def __init__(self, file_path: str):
        super().__init__()
        self._initialize_consumers(file_path)

    def _initialize_consumers(self, file_path: str):
        consumers_dataframe = csv_processor.read(file_path)
        self._consumers = [Consumer(data) for data in consumers_dataframe.values]

    def get_states(self):
        return [consumer.state for consumer in self._consumers]

    def create_chart(self, chart_type, has_to_be_downloaded, max_quantity=10):
        states = self.get_states()
        state_counter = Counter(states)
        sorted_dict_values = dict(sorted(state_counter.items(), key=lambda item: item[1], reverse=True)[:max_quantity])

        if chart_type == 'bar':
            self._create_bar_chart(state_counter, has_to_be_downloaded)
        elif chart_type == 'pie':
            self._create_pie_chart(sorted_dict_values, has_to_be_downloaded)
        elif chart_type == 'combined':
            self._create_combined_chart(state_counter, sorted_dict_values, has_to_be_downloaded)

    def _create_bar_chart(self, state_counter, has_to_be_downloaded):
        plt.figure(figsize=(8, 7))
        plt.bar(state_counter.keys(), state_counter.values(), color='green')

        self._save_or_show_plot(has_to_be_downloaded, 'state-bar-chart.png', 'Bar Chart', 'States', 'Frequency',
                                rotation=-90)

    def _create_pie_chart(self, sorted_dict_values, has_to_be_downloaded):
        labels, sizes = zip(*sorted_dict_values.items())
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

        self._save_or_show_plot(has_to_be_downloaded, 'state-pie-chart.png', 'Pie Chart')

    def _create_combined_chart(self, state_counter, sorted_dict_values, has_to_be_downloaded):
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))

        ax1.bar(state_counter.keys(), state_counter.values(), color='green')
        ax1.set_title('Bar Chart')
        ax1.set_xlabel('States')
        ax1.set_ylabel('Frequency')
        ax1.tick_params(axis='x', rotation=45)

        labels, sizes = zip(*sorted_dict_values.items())
        ax2.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax2.set_title('Pie Chart')

        plt.tight_layout()

        self._save_or_show_plot(has_to_be_downloaded, 'combined-chart.png')

    @staticmethod
    def _save_or_show_plot(has_to_be_downloaded, filename, title, xlabel=None, ylabel=None, rotation=None):
        if has_to_be_downloaded:
            plt.savefig(f'./files/{filename}')
        plt.title(title)
        if xlabel:
            plt.xlabel(xlabel)
        if ylabel:
            plt.ylabel(ylabel)
        if rotation is not None:
            plt.xticks(rotation=rotation)
        plt.show()
